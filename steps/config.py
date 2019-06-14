import os
import time
import settings

'''
Generates folders and config files for each device in lists
'''

def check():
    params = settings.get()
    template = params['template']

    if not os.path.isdir("config"):
        print("No config directory found, creating directry...")
        try:
            os.mkdir('config')
        except OSError:
            print("Failed to create config directory")
        else:  
            print("Created config directory")

    while True:
        if not os.path.exists(template):
            print("{} not found, copy template file there or change config to suit".format(template))
            input("Press ENTER to continue...")
        else:
            return(True, params)
    


def generate(name, ip):
    exists, params = check()
    if exists:
        hostname = '{}{}{}'.format(params['prefix'], name, params['suffix'])
        with open(params['template']) as f:
            blank_config = f.read()
            new_config = blank_config.format(hostname=hostname, ip=ip)
        
        new_file = 'config/{}.txt'.format(hostname)

        if os.path.exists(new_file):
            while True:
                overwrite = input("'/{}' exists, overwrite? (y/n)".format(new_file))
                if overwrite == 'y':
                    break
                if overwrite == 'n':
                    print("Leaving existing config as is.")
                    return(True)
                else:
                    print("Type y or n")

        with open(new_file, 'w') as nf:
            nf.write(new_config)
            nf.close()
        print("Created config '/{}'".format(new_file))        
        return(True)

         

            


if __name__ == '__main__':
    os.chdir('..')
    generate('test', '10.11.12.13')
