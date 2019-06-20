import os
from shutil import copyfile

"""
Parses settings text file
Generates file if it doesn't exist
"""

def get():
    line_count = 0
    settings = {}
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
                    generate()
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
        try:
            open('settings/settings.txt','a').close()
            print("Created blank settings file.")
        except:
            print("Failed to create settings.txt file")
    backup()
    

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
            f.write('com=\ntemplate=command\nprefix=cb-\nsuffix=-wgb\nfirmware=tftp/ap3g2-k9w7-tar.153-3.JI1.tar\npc_ip=10.0.0.5\nwgb_ip=10.0.0.2')
            f.close()
            print("Set default parameters.")
        get()
    else:
        generate()

def wizard():
    print("Gathering some info, this only needs to be done once...")
    while True:
        manualCom = input("Manually specify COM port (m) or scan ports (s): ")
        if manualCom == 'm':
            com = input("Enter COM port (e.g COM1): ")
            if com[:3] == 'COM' and isinstance(com[4], int):
                break
            elif len(com) == 1 and isinstance(com, int):
                com = 'COM{}'.format(com)
                break
            else:
                print("Unreconised COM port, try again you silly billy")
        elif manualCom == 's':
            com = ''
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
                    break
                else:
                    input("Couldn't match the filename, try again [ENTER]")
            break


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