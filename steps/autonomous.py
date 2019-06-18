if __name__ == "__main__":
    import sys
    sys.path.append("..")

import time
from commands import close, com, credentials, initialize, match, read, write



def check(console):
    '''
    Checks if autonomous
    '''
    print("Checking if autonomous")
    while True:
        prompt = read.serial(console)
        if prompt:
            if len(prompt[0]) == 3:
                if prompt[0] == 'ap>' or  prompt[0] == 'ap#':
                    print('Autonomous')
                    return(True)
            elif len(prompt[0]) >= 10:
                if prompt[0][:2] == 'AP':
                    if prompt[0][-1:] == '>' or  prompt[0][-1:] == '#':
                        print('Not autonomous')
                        return(False)

                elif prompt[0][-9:] == '-command#' or prompt[0][-7:] == '-fleet#':
                        print('Autonomous')
                        return(True)
                elif prompt[0][-9:] == '-command>' or prompt[0][-7:] == '-fleet>':
                        print('Autonomous')
                        return(True)
                elif prompt[0][-1] == '>' or prompt[0][-1] == '#':
                    print('Autonomous')
                    return(True)   
            elif len(prompt[0]) == 9:
                if prompt[0][:9] == 'Username:':
                    print('Autonomous')
                    return(True)
                else:
                    print("Unreconized prompt")

        else:
            write.serial(console, "\r")
            time.sleep(1)


def convert(console):
    write.serial(console, '\r')
    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "debug capwap console cli")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, 'capwap ap autonomous')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, 'yes')
                prompt = read.serial(console)
                time.sleep(1)
                print('Stating autonomous conversion')
                return(True)
            elif prompt[0][-1:] == '>':
                print('Not Logged in')
                return(False)
            else:
                write.serial(console, '\r')
        else:
            write.serial(console, '\r')


if __name__ == "__main__":
    check(initialize.open('COM1'))