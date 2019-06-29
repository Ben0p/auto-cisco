import os
import time
from steps import parameters

'''
Generates a config from a template specified in settings.txt
'''

def check():
    params = parameters.get()
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
        if not os.path.exists('{}'.format(template)):
            print("{} not found, copy template file there or change config to suit".format(template))
            input("Press ENTER to continue...")
        else:
            return(params)
    


def generate(vehicle):
    params = check()
    name = vehicle[0].lower()
    ip = vehicle[1]
    if params:
        hostname = '{}{}{}'.format(params['prefix'], name, params['suffix'])
        while True:
            try:
                with open('{}'.format(params['template'])) as f:
                    blank_config = f.read()
                    new_config = blank_config.format(hostname=hostname, ip=ip)
                    break
            except:
                input("Unable to generate config, ensure the template has {hostname} and {ip} then press ENTER")

        
        new_file = 'config/{}.txt'.format(hostname)

        if os.path.exists(new_file):
            while True:
                overwrite = input("'/{}' exists, overwrite? (y/n): ".format(new_file))
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

         
def exists(vehicle):
    params = parameters.get()
    filename = 'config/{}-{}-{}.txt'.format(params['prefix'], vehicle[0], params['suffix'])

    try:
        files = os.listdir('config')
        if filename in files:
            return(filename)
        else:
            return(False)
    except:
        return(False)




if __name__ == '__main__':
    os.chdir('..')
    generate(['test', '10.11.12.13'])
