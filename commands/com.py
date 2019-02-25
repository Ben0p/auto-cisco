
import serial
from pathlib import Path
import os



def settingsExist():
    settings = './settings/settings.txt'

    settings_file = Path(settings)
    if settings_file.is_file():
        return(True)
    else:
        print("No existing settings found")
        if not os.path.exists('./settings'):
            os.makedirs('./settings')
        return(False)

def getSettings():
    with open('./settings/settings.txt', 'r') as f:
        for line in f:
            stripped = line.strip()
            com = stripped.split('=')[1]
        f.close()
    print('Retrieved {} from settings'.format(com))
    return(com)



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
                if user_COM[:3] == 'COM':
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

def saveSettings(com):
    with open('./settings/settings.txt', 'w') as f:
        settings = 'com={}'.format(com)
        f.write(settings)
        f.close()




def get():

    if settingsExist():
        com = getSettings()
        return(com)
    else:
        com = getCOM()
        saveSettings(com)
        return(com)
    






if __name__ == '__main__':
    get()