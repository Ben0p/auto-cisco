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
        print("No settings file found, creating file...")
        try:
            open('settings/settings.txt','a').close()
            print("Created blank settings file.")
        except:
            print("Failed to create settings.txt file")
    populate()
    

def populate():
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