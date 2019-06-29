import time
from commands import close, com, credentials, initialize, match, read, write
from steps import parameters, tftp


def check(console):
    '''
    Checks configuration status
    '''
    print('Checking configuration')

    params = parameters.get()

    while True:
        prompt = read.serial(console)
        if prompt:
            if len(prompt[0]) == 3:
                if prompt[0] == 'ap>' or  prompt[0] == 'ap#':
                    print('Not configured')
                    return(False)
            elif prompt[0][:2] == 'AP':
                if prompt[0][-1:] == '>' or  prompt[0][-1:] == '#':
                    print('Not configured')
                    return(False)

            elif len(prompt[0]) >= 9:
                if prompt[0][-1] == '#' or prompt[0][-1] == '>':
                    if prompt[0].startswith(params['prefix']) and prompt[0].endswith(params['suffix']):
                        print("Already configured as {}".format(prompt[0]))
                        return('something')
                    else:
                        print('Unable to detect current configuration.')
                        return('something')

            elif any("--More--" in s for s in prompt):
                write.serial(console, ' ')

        else:
            write.serial(console, "\r")
            time.sleep(1)

def copy(console, vehicle):
    params = parameters.get()
    name = vehicle[0].lower()

    conf_file = '{}{}{}.txt'.format(params['prefix'],name,params['suffix'])

    waiting = False

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "copy tftp://10.0.0.5/config/{} flash:".format(conf_file))
                time.sleep(1)
                prompt = read.serial(console)
                write.serial(console, "\r")
                time.sleep(3)
                prompt = read.serial(console)
            elif prompt[0][:9] == 'Accessing':
                print("waiting...")
                waiting = True
                prompt = read.serial(console)
                time.sleep(4)
                prompt = read.serial(console)

            elif any("(Timed out)" in s for s in prompt):
                if prompt[0][-11:] == '(Timed out)':
                    while True:
                        try_again = input("TFTP Timed out, try again? (y/n): ")
                        if try_again == 'y':
                            break
                        elif try_again == 'n':
                            print("Aborting...")
                            return(False)
                        else:
                            print("I said y or n")

            elif any("[OK - " in s for s in prompt):
                print("OK Detected")
                waiting = False
                return(True)
            
            elif any("Do you want to over write? [confirm]" in s for s in prompt):
                print("Overwriting")
                write.serial(console, "\r")
                time.sleep(1)
                return(True)
        else:
            write.serial(console, "\r")
            time.sleep(1)



def load(console, vehicle):

    print("Loading config to running-config")
    name = vehicle[0].lower()
    params = parameters.get()

    conf_file = '{}{}{}.txt'.format(params['prefix'],name,params['suffix'])

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "copy flash:{} run".format(conf_file))
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                time.sleep(2)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(2)
                prompt = read.serial(console)
                write.serial(console, 'wr mem')
                time.sleep(1)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                print("Configured as {}".format(name))
                return(True)
        else:
            write.serial(console, "\r")


def overWrite():
    while True:
        overwrite = input("Unit already configured, do you wish to overwrite? (y/n): ")
        if overwrite == 'y':
            return(True)
        elif overwrite == 'n':
            return(False)
        else:
            print("Enter y or n ")            
