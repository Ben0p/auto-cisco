import time
from commands import *


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
                    break
            elif len(prompt[0]) >= 10:
                if prompt[0][:2] == 'AP':
                    if prompt[0][-1:] == '>' or  prompt[0][-1:] == '#':
                        print('Not autonomous')
                        return(False)
                        break

                elif prompt[0][-9:] == '-command#' or prompt[0][-7:] == '-fleet#':
                        print('Autonomous')
                        return(True)
                        break
                elif prompt[0][-9:] == '-command>' or prompt[0][-7:] == '-fleet>':
                        print('Autonomous')
                        return(True)
                        break

        else:
            write.serial(console, "\r")


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
                break
            elif prompt[0][-1:] == '>':
                print('Not Logged in')
                return(False)
                break
            else:
                write.serial(console, '\r')
        else:
            write.serial(console, '\r')