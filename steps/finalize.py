import time
import random
from commands import close, com, credentials, initialize, match, read, write
from steps import parameters


names = [
    'Silv',
    'Ben0',
    'bhebhe',
    'Kyle',
    'Grant',
    'John',
    'Rupert',
    'Dan',
    'Doggy',
    'Glen',
    'Paul',
    'Craig',
    'Roy',
    'Steve'
    ]


def finish(console, vehicle):
    params = parameters.get()

    hostname = '{}{}{}'.format(params['prefix'], vehicle[0], params['suffix'])

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "wr mem")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                print("Config written to memory")
                write.serial(console, '\r')
                time.sleep(2)
                prompt = read.serial(console)
                configured_name = prompt[0][:-1]
                close.serial(console)
                break

        else:
            write.serial(console, "\r")

    
    try_agian = 'n'

    if configured_name != hostname:
        print("!!WARNING!!")
        print('Configured hostname DOES NOT match specified vehicle [FAIL]')
        print("Configured:  {}".format(configured_name))
        print("Specified:   {}".format(vehicle[0]))

        while True:
            try_again = input("Try again (y) or ignore (n): ")
            if try_again == 'n':
                break
            elif try_again == "y":
                break
            else:
                print("How hard is it to press y or n")
    
        
    if configured_name == hostname or try_again == 'n':
        print("--------------------------------------")
        print("CONGRATULATIONS! MADE IT TO THE END!")
        print("Check config via putty.")
        print("Don't forget to update records")
        print("--------------------------------------")
        print('--------------------------------------')
        print('   VEHICLE:     {}'.format(vehicle[0]))
        print('        IP:     {}'.format(vehicle[1]))
        print('  HOSTNAME:     {}'.format(hostname))
        print('--------------------------------------')
        print('')
        print('Milkshakes are on {}'.format(random.choice(names)))
        input('Ready for another round? [ENTER]')
    
