import time
from commands import close, com, credentials, initialize, match, read, write



def command(console):
    '''
    Pings command gateway
    '''

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-8:] == 'command#' or prompt[0][-8:] == 'command>':
                    write.serial(console, "ping 10.221.64.1")
                    prompt = read.serial(console)
                    time.sleep(1)
                    write.serial(console, '\r')
                    time.sleep(5)
                    prompt = read.serial(console)
                    if any('!!!!!' in s for s in prompt):
                        print("Ping OK")
                        return(True)
                        break

        else:
            write.serial(console, "\r")