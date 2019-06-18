import time
from commands import close, com, credentials, initialize, match, read, write



def command(console):
    '''
    Pings command gateway
    '''
    failedPing = 0

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == '#' or prompt[0][-1:] == '>':
                    write.serial(console, "ping 10.221.64.1")
                    prompt = read.serial(console)
                    time.sleep(1)
                    write.serial(console, '\r')
                    time.sleep(5)
                    prompt = read.serial(console)
                    if any('!!!!!' in s for s in prompt):
                        print("Ping OK")
                        return(True)
            if prompt[0] == '.':
                failedPing += 1
            if failedPing == 5:
                failedPing = 0
                print("Ping Timeout")
                tryAgain = input("Try again (y) or ignore (n): ")
                if tryAgain == "y":
                    continue
                else:
                    return(True)

        else:
            write.serial(console, "\r")
            time.sleep(1)