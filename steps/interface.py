import time
from commands import *



def check(console):
    '''
    Checks if ip interface configured
    '''

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#" or prompt[0][-1:] == ">":
                write.serial(console, "sh ip int br")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                if any('10.0.0.2' in s for s in prompt):
                    print("Interface set for 10.0.0.2")
                    return(True)
                    break
                else:
                    print("Interface not set.")
                    return(False)
                    break
        else:
            write.serial(console, "\r")


def configure(console):
    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "conf t")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, "int bvi1")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, "ip address 10.0.0.2 255.255.255.0")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, "exit")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, "exit")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                prompt = read.serial(console)
                time.sleep(1)
                print("Interface configured")
                return(True)
            else:
                print("Not enabled.")
                return(False)
                break
        else:
            write.serial(console, "\r")