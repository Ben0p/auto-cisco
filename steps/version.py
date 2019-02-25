import time
from commands import *


def check(console):
    '''
    Checks if upgraded or not
    '''

    old_ver = 'Version 15.3(3)JF5, RELEASE SOFTWARE (fc2)'
    new_ver = 'Version 15.3(3)JI1, RELEASE SOFTWARE (fc1)'

    print("Checking software version...")
    while True:

        prompt = read.serial(console)
        if prompt:
            if prompt[0][:2] == 'AP':
                if prompt[0][-1:] == '>' or  prompt[0][-1:] == '#':
                    write.serial(console, "sh ver")
            elif prompt[0] == 'ap>' or prompt[0] == 'ap#':
                write.serial(console, "sh ver")
            elif len(prompt[0]) >= 10:
                if prompt[0][-9:] == '-command#' or prompt[0][-7:] == '-fleet#':
                        print('Upgraded')
                        return(True)
                        break
                elif prompt[0][-9:] == '-command>' or prompt[0][-7:] == '-fleet>':
                        print('Upgraded')
                        return(True)
                        break


            if any(new_ver in s for s in prompt):
                print('Upgraded')
                return(True)
            elif any(old_ver in s for s in prompt):
                print('Not Upgraded')
                return(False)
            elif any("--More--" in s for s in prompt):
                write.serial(console, ' ')

        else:
            write.serial(console, "\r")

def upgrade(console):
    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "archive download-sw /overwrite /force-reload tftp://10.0.0.5/ap3g2-k9w7-tar.153-3.JI1.tar")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                print("Transferring image and upgrading...")
                prompt = read.serial(console)
                time.sleep(1)
                return(True)
                break
            else:
                print("Not enabled.")
                return(False)
                break
        else:
            write.serial(console, "\r")