import time
from commands import close, com, credentials, initialize, match, read, write


def check(console):
    '''
    Checks if in enable
    '''

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == ">":
                write.serial(console, "en")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, credentials.password)
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
            elif prompt[0][-1:] == "#":
                print("Enabled")
                return(True)
                break
        else:
            write.serial(console, "\r")