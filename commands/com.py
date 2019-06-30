
import serial
from pathlib import Path
import os
from steps import parameters



def getSettings():
    settings = parameters.get()
    com = settings['com']
    if com:
        return(com)
    else:
        return(False)


def getCOM():

    print('Scanning COM ports...')
    ports = ['COM%s' % (i + 1) for i in range(256)]
    active = []

    while True:
        for port in ports:
            try:
                print("Testing port %s" % (port))
                ser = serial.Serial(port,9600,timeout=1.5)
                for _ in range(3):
                    ser.readline().decode("utf-8")
                ser.close()
                active.append(port)
            except (OSError, serial.SerialException):
                pass
        print("Active ports = {}".format(active))
        if len(active) > 1:
            while True:
                user_COM = input('{} active COM ports, choose port ({})...'.format(len(active), active[0]))
                if user_COM[:3] == 'COM' and isinstance(int(user_COM[3:]), int):
                    return(user_COM)
                elif len(user_COM) == 1 and isinstance(int(user_COM), int):
                    print("Using COM{}".format(user_COM))
                    user_COM = 'COM{}'.format(user_COM)
                    return(user_COM)
                else:
                    print('Port number must start with COM')

        elif len(active) == 0:
            user_input = input('No active COM ports found, check your setup bro and press enter to continue')
            if user_input == '':
                continue

        elif len(active) == 1:
            user_input = input('One port found ({}), is this correct? (y/n)'.format(active[0]))
            while True:
                if user_input == 'y':
                    return(active[0])
                elif user_input == 'n':
                    while True:
                        user_COM = input('Enter COM port number (COMx)')
                        if user_COM[:3] == 'COM':
                            return(user_COM)
                        else:
                            print('Port number must start with COM')


    return(active)




def get():

    com = getSettings()
    if com:
        return(com)
    else:
        com = getCOM()
        parameters.update('com', com)
        return(com)
    






if __name__ == '__main__':
    get()