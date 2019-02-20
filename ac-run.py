import ac_com
import ac_serial
import serial
import time

'''
Main auto-cisco run file
'''
#
def step1(com):
    print('Step 1')
    ser = ac_serial.initSerial(com)

    upgraded = False

    for x in range(3):
        ac_serial.write(ser, b'\r')
        time.sleep(0.5)

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)
        else:
            ac_serial.write(ser, b'\r')

        if line == "ap>":
            autonomous = True
            if upgraded == False:
                ac_serial.write(ser, b'sh ver\r')
                print(ac_serial.read(ser))
            else:
                break
        if line == "ap#":
            ac_serial.write(ser, b'exit\r')
            print(ac_serial.read(ser))
        if line == 'Press RETURN to get started.':
            ac_serial.write(ser, b'\r')
        
        if line[-8:] == '--More--':
            ac_serial.write(ser, b' ')

        if line[-42:] == "Version 15.3(3)JI1, RELEASE SOFTWARE (fc1)":
            upgraded = True
        
        if line[-13:] == 'image version':
            ac_serial.write(ser, b'\r')

    ser.close()
    return(autonomous, upgraded)


# In autonomous mode
def step2(com):
    ser = ac_serial.initSerial(com)

    logged_in = False
    heater_msg = False
    autonomous = False

    count = 0
    for x in range(3):
        ac_serial.write(ser, b'\r')
    while True:
        try:
            line = ac_serial.read(ser)
        except:
            ac_serial.write(ser, b'\r')
            time.sleep(1)
        if line:
            print(line)

        if logged_in:
            if line == 'ap>':
                break
        else:
            if line[-22:] == 'existing image version':
                ac_serial.write(ser, b'\r')
                heater_msg = True
            if heater_msg:
                    if line == 'ap>':
                        autonomous = True
                        ac_serial.write(ser, b'login\r')
                        time.sleep(3)
                    if line[:9] == 'Username:':
                        ac_serial.write(ser, b'cisco\r')
                        time.sleep(3)
                    if line[:9] == 'Password:':
                        ac_serial.write(ser, b'Cisco\r')
                        logged_in = True
    ser.close()

# Setting ip
def step3(com):
    print('Step 3')
    ser = ac_serial.initSerial(com)

    enable = False
    conft = False

    for x in range(3):
        ac_serial.write(ser, b'\r')

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)

        if enable == True:

            if conft:
                if line[:11] =='ap(config)#':
                    time.sleep(1)
                    ac_serial.write(ser, b'int bvi1\r')
                
                elif line[:14] == 'ap(config-if)#':
                    time.sleep(1)
                    ac_serial.write(ser, b'ip address 10.0.0.2 255.255.255.0\r')
                    print(ac_serial.read(ser))
                    time.sleep(1)
                    ac_serial.write(ser, b'exit\r')
                    print(ac_serial.read(ser))
                    time.sleep(1)
                    ac_serial.write(ser, b'exit\r')
                    print(ac_serial.read(ser))
                    break
            
            elif line == 'ap#':
                ac_serial.write(ser, b'conf t\r')
                conft = True
                    

        else:
            if line == 'ap>':
                ac_serial.write(ser, b'en')
                ac_serial.write(ser, b'\n')
                time.sleep(1)

    
            if line[:9] == 'Password:':
                time.sleep(1)
                ac_serial.write(ser, b'Cisco')
                time.sleep(0.5)
                ac_serial.write(ser, b'\n')
                enable = True


def step4(com):
    print('Step 4')
    ser = ac_serial.initSerial(com)


    for x in range(3):
        ac_serial.write(ser, b'\r')

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)
        
        if line == 'ap#':
            time.sleep(1)
            ac_serial.write(ser, b'archive download-sw /overwrite /force-reload tftp://10.0.0.5/ap3g2-k9w7-tar.153-3.JI1.tar')
            time.sleep(1)
            ac_serial.write(ser, b'\r')
        elif line[-18:] == 'console by console':
            time.sleep(1)
            ac_serial.write(ser, b'\r')
        elif line[-22:] == 'existing image version':
            break

def step5(com):
    print('Step 5')
    ser = ac_serial.initSerial(com)


    for x in range(3):
        ac_serial.write(ser, b'\r')

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)
        
        if line == 'ap>':
            ac_serial.write(ser, b'en')
            ac_serial.write(ser, b'\n')
            time.sleep(1)
        if line[:9] == 'Password:':
            time.sleep(1)
            ac_serial.write(ser, b'Cisco')
            time.sleep(0.5)
            ac_serial.write(ser, b'\n')
        if line == 'ap#':
            break
    
    name = input("Enter vehicle name (DT201): ")

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)


def main():
    com = ac_com.get()
    autonomous, upgraded = step1(com)
    if autonomous and upgraded:
        print('In autonomous')
        print('Upgraded')
        step5(com)
    elif autonomous and not upgraded:
        print("Autonomous")
        print("Not upgraded")
        step4(com)
    else:
        print("Not autonomous")
        print("Not upgraded")
        step2(com)

if __name__ == "__main__":
    main()