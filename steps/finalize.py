import time
import random
from commands import close, com, credentials, initialize, match, read, write


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
    ]


def finish(console, vehicle):
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
                configured_name = prompt[0].split('-')[1]
                close.serial(console)
                break

            else:
                print("Not enabled.")
                return(False)
                break
        else:
            write.serial(console, "\r")

    if configured_name.upper() == vehicle[0]:
        print('Configured hostname matches specified vehicle [OK]')
        print("--------------------------------------")
        print("CONGRATULATIONS! MADE IT TO THE END!")
        print("Configured as COMMAND")
        print("Check config via putty.")
        print("Don't forget to record serial and MAC")
        print("--------------------------------------")
        print('--------------------------------------')
        print('   VEHICLE:     {}'.format(vehicle[0]))
        print('COMMAND IP:     {}'.format(vehicle[1]))
        print('  FLEET IP:     {}'.format(vehicle[2]))
        print('--------------------------------------')
        print('')
        print('Milkshakes are on {}'.format(random.choice(names)))
        input('Ready for another round? [ENTER]')

    elif configured_name.upper() != vehicle[0]:
        print('Configured hostname DOES NOT match specified vehicle [FAIL]')
        print("Configured:  {}".format(configured_name.upper()))
        print("Specified:   {}".format(vehicle[0]))
        print("ABORTING...")
        input("Try again? [ENTER]")

