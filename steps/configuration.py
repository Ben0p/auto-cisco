import time
from commands import close, com, credentials, initialize, match, read, write


def check(console):
    '''
    Checks configuration status
    '''
    print('Checking configuration')

    while True:
        prompt = read.serial(console)
        if prompt:
            if len(prompt[0]) == 3:
                if prompt[0] == 'ap>' or  prompt[0] == 'ap#':
                    print('Not configured')
                    return(False, 'None')
                    break
            elif prompt[0][:2] == 'AP':
                if prompt[0][-1:] == '>' or  prompt[0][-1:] == '#':
                    print('Not configured')
                    return(False, 'None')
                    break
            elif prompt[0][:3] == 'cb-':
                if prompt[0][-7:] == '-fleet#' or prompt[0][-7:] == '-fleet>':
                    print("Configured as fleet")
                    return(True, 'fleet')
                    break
                if prompt[0][-9:] == '-command#' or prompt[0][-9:] == '-command>':
                    print("Configured as command")
                    return(True, 'command')
                    break
            elif any("--More--" in s for s in prompt):
                write.serial(console, ' ')

        else:
            write.serial(console, "\r")

def copy(console, vehicle):
    name = vehicle[0].lower()
    command_file = 'cb-{}-command.txt'.format(name)
    fleet_file = 'cb-{}-fleet.txt'.format(name)

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "copy tftp://10.0.0.5/{} flash:".format(fleet_file))
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                time.sleep(1)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                write.serial(console, "copy tftp://10.0.0.5/{} flash:".format(command_file))
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                time.sleep(1)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                print("Configs copied")
                return(True)
            else:
                print("Not enabled.")
                return(False)
                break
        else:
            write.serial(console, "\r")


def command(console, vehicle):
    name = vehicle[0].lower()
    command_file = 'cb-{}-command.txt'.format(name)

    while True:
        prompt = read.serial(console)
        if prompt:
            if prompt[0][-1:] == "#":
                write.serial(console, "copy flash:{} run".format(command_file))
                prompt = read.serial(console)
                time.sleep(1)
                write.serial(console, '\r')
                time.sleep(2)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(2)
                prompt = read.serial(console)
                write.serial(console, 'wr mem')
                time.sleep(1)
                prompt = read.serial(console)
                write.serial(console, '\r')
                time.sleep(4)
                prompt = read.serial(console)
                print("Configured as command")
                return(True)
            else:
                print("Not enabled.")
                return(False)
                break
        else:
            write.serial(console, "\r")