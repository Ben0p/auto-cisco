import time
from commands import read, write, credentials

def now(console):
    write.serial(console, '\r')
    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == ">":
                write.serial(console, "login\r")
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '{}\r'.format(credentials.username))
                prompt = read.serial(console)
                time.sleep(3)
                write.serial(console, '{}\r'.format(credentials.password))
                prompt = read.serial(console)
                time.sleep(3)
                write.serial(console, '{}\r'.format('en'))
                prompt = read.serial(console)
                time.sleep(3)
                write.serial(console, '{}\r'.format(credentials.password))
                prompt = read.serial(console)
                time.sleep(3)
                print('Logged in')
                return(True)
            elif prompt[0][-1:] == '#':
                print('Logged in')
                return(True)
            elif prompt[0][:9] == 'Username:':
                write.serial(console, '{}\r'.format(credentials.configured_username))
                prompt = read.serial(console)
                time.sleep(3)
                write.serial(console, '{}\r'.format(credentials.configured_password))
                prompt = read.serial(console)
                time.sleep(3)
                write.serial(console, '{}\r'.format('en'))
                prompt = read.serial(console)
                time.sleep(3)
                write.serial(console, '{}\r'.format(credentials.configured_password))
                prompt = read.serial(console)
                time.sleep(3)
                print('Logged in')
                return(True)
            else:
                write.serial(console, '\r')
                time.sleep(1)




