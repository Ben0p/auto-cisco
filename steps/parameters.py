import os
from shutil import copyfile
from steps import ip
from commands import com
import re
import ipaddress
from netaddr import IPNetwork, IPAddress

"""
Parses settings text file
Generates file if it doesn't exist
"""
settings = {}

def get():
    required_settings = ['template', 'hostname', 'ip', 'prefix', 'suffix', 'case', 'temp', 'test', 'com']
    line_count = 0
    while True:
        if os.path.isdir("settings"):
            if os.path.exists("settings/settings.txt"):
                with open('settings/settings.txt') as f:
                    for line in f:
                        line_count =+ 1
                        line = line.strip()
                        line = line.split('=')
                        setting = line[0]
                        param = line[1]
                        settings[setting] = param
                if line_count == 0:
                    print("Config is blank, populating parameters...")
                    missing_setting = False
                    generate()
                elif line_count > 0:
                    settings_in_file = []
                    for key, value in settings.items():
                        settings_in_file.append(key)
                    if len(settings_in_file) < len(required_settings):
                        missing_setting = True
                    else:
                        missing_setting = False
                    
                if missing_setting:
                    print("Required settings missing in settings file, starting wizard")
                    generate()
                    missing_setting = False
                return(settings)
            else:
                print("settings/settings.txt not found, creating file...")
                generate()
        else:
            print("No settings directory found, creating directory...")
            generate()


def generate():
    if not os.path.isdir("settings"):
        try:
            os.mkdir('settings')
        except OSError:
            print("Failed to create settings directory")
        else:  
            print("Created settings directory")

    if not os.path.exists("settings/settings.txt"):
        print("No settings file found, initiating wizard jizz")
        wizard()

    else:
        backup()
        wizard()
    print("You are a wizard Harry")
    

def backup():
    """
    Populates blank settings in settings file for user to amend
    """
    
    lines = 0
    if os.path.exists("settings/settings.txt"):
        with open('settings/settings.txt', 'r+') as f:
            for line in f:
                lines += 1
            if lines > 1:
                copyfile("settings/settings.txt", "settings/settings.back")
            f.close()


def wizard():
    print("Gathering some info, this only needs to be done once...")
    while True:
        manualCom = input("Manually specify COM port (m) or scan ports (s): ")
        if manualCom == 'm':
            comp = input("Enter COM port (e.g COM1 or 1): ")
            if comp[:3] == 'COM' and isinstance(int(comp[3:]), int):
                settings['com'] = comp
                break
            elif len(comp) == 1 and isinstance(int(comp), int):
                print("Using COM{}".format(comp))
                comp = 'COM{}'.format(comp)
                settings['com'] = comp
                break
            else:
                print("Unreconised COM port, try again you silly billy")
        elif manualCom == 's':
            comp = com.getCOM()
            settings['com'] = comp
            break

    while True:
        manualTemplate = input("Manually specify config template (m) or scan current folder (s): ")
        if manualTemplate == 'm':
            template = input("Enter template name: ")
            files = scanFiles()
            if template in files:
                print("Found template {}, verrifying...".format(template))
                try:
                    config = open(template, 'r').read()
                    config.format(hostname='testonly', ip='10.11.12.13')
                    print("Template ok")
                    settings['template'] = template
                    break
                except:
                    print("Couldn't parse template, ensure it has {hostname} and {ip}")
            else:
                print("Couldn't find template, try again buddy")
        elif manualTemplate == 's':
            files = scanFiles()
            print(files)
            while True:
                template = input('Type in the template filename as above: ')
                if template in files:
                    print("Got that")
                    settings['template'] = template
                    break
                else:
                    input("Couldn't match the filename, try again [ENTER]")
            break

    while True:
        hostname, ips = ip.get()
        settings['hostname'] = hostname
        ip_addr = input("Type IP address that the WGB is connected to or (t) to try again: ")
        valid_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_addr)
        if ip_addr == 't':
            continue
        elif valid_ip:
            print("Ok, will use {}".format(ip_addr))
            settings['ip'] = ip_addr
            break
        else:
            print("Unreconised IP, or press (t)")

    while True:
        octets = ip_addr.split('.')
        suggested_ip = int(octets[-1])+1
        suggested_ip = '{}.{}.{}.{}'.format(octets[0], octets[1], octets[2], suggested_ip)
        temp_ip = input("Enter temporary IP address for 3702 ({}): ".format(suggested_ip))
        valid_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",temp_ip)
        if valid_ip:
            if IPAddress(temp_ip) in IPNetwork('{}/24'.format(ip_addr)):
                print("{} is within /24 range OK".format(temp_ip))
                settings['temp'] = temp_ip
                break
            else:
                print("{} not within /24 range of {}, try agian.".format(temp_ip, ip_addr))
                continue
        else:
            print("Unreconised IP, or press (t)")
    
    while True:
        test_ip = input("Enter IP for ping test once configured (gateway): ")
        valid_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",test_ip)
        if valid_ip:
            print("{} seems legit".format(test_ip))
            settings['test'] = test_ip
            break
        else:
            print("IP not valid")

    while True:
        prefix = input("Enter standard prefix e.g. 'cb-' : ")
        suffix = input("Enter standard suffix e.g. '-wgb' : ")
        case = input("Uppercase (u) or lowercase (l): ")
        if case == 'u':
            example_hostname = '{}name{}'.format(prefix,suffix).upper()
            case = 'upper'
        elif case == 'l':
            example_hostname = '{}name{}'.format(prefix,suffix).lower()
            case = 'lower'
        else:
            print("You've gone and stuffed up, starting again...")
            continue
        confirmed_hostname = input("Example hostname '{}', looks good? (y/n): ".format(example_hostname))
        if confirmed_hostname == 'y':
            settings['prefix'] = prefix
            settings['suffix'] = suffix
            settings['case'] = case
            break
        elif confirmed_hostname == 'n':
            print("Bugger aye, starting again...")
            continue
        else:
            print("Bro, I don't know what you are wanting to do here...")
            continue
        


    with open('settings/settings.txt', 'w') as f:
            for key, value in settings.items():
                f.write("{}={}\n".format(key,value))



def scanFiles():
    f = []
    fl = []
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        f.extend(filenames)
        break
    for (dirpath, dirnames, filenames) in os.walk('config'):
        for filename in filenames:
            f.append('config/{}'.format(filename))
        break
    
    for _file in f:
        split = _file.split('.')
        if len(split) == 2:
            if split[1] == 'txt':
                fl.append(_file)
        elif len(split) == 1:
            fl.append(_file)

    return(fl)

def update(param, value):
    settings = get()
    settings[param] = value
    copyfile("settings/settings.txt", "settings/settings.back")
    with open('settings/settings.txt', 'w') as f:
        for key in settings:
            f.write('{}={}\n'.format(key, settings[key]))
        f.close()


if __name__ == "__main__":
    os.chdir('..')
    get()