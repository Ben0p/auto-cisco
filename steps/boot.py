import time
from commands import close, com, credentials, initialize, match, read, write


def check(console):
    '''
    Check if finished booting, otherwise print bootup
    '''
    print("Checking boot status...")
    while True:
        prompt = read.serial(console)

        if prompt:
            if match.boot(prompt[0]):
                print("Booted")
                return(True)
                break
            elif any("--More--" in s for s in prompt):
                write.serial(console, ' ')
        else:
            write.serial(console, '\r')
            time.sleep(3)
            