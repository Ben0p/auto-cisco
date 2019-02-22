import ac_com
import ac_serial
import serial
import time

'''
Main auto-cisco run file
'''
#

def step0():
    
        while True:
            name = input("Enter vehicle name (DT201): ")
            with open('./lists/master.csv', 'r') as f:
                for line in f:
                    stripped = line.strip()
                    split = stripped.split(',')
                    if split[0] == name:
                        user_input = input('Matched {}\nFleet IP {}\nCommand IP {}\nIs this correct? (y/n)'.format(split[0],split[2],split[1]))
                        if user_input == 'y':
                            print('!!! Power up IW3702 now !!!')
                            return(split)
                        elif user_input == 'n':
                            print("Try again...")
                            continue
                        else:
                            pass
            print("No Match")


def step1(com):
    print('Checking status....')
    while True:
        try:
            ser = ac_serial.initSerial(com)
            break
        except serial.serialutil.SerialException:
            input("Serial port in use, close putty.")


    upgraded = False
    loaded = False
    command = False
    fleet = False

    sw_ver = 'None'

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
            time.sleep(1)

        if line == "ap>":
            autonomous = True
            if upgraded == False:
                time.sleep(1)
                ac_serial.write(ser, b'sh ver')
                time.sleep(1)
                line = ac_serial.read(ser)
                print(line)
                time.sleep(2)
                ac_serial.write(ser, b'\r')
                sw_ver = ac_serial.read(ser)
                print('-----')
                print(sw_ver)
                print('-----')
                if sw_ver[-42:] == "Version 15.3(3)JI1, RELEASE SOFTWARE (fc1)":
                    upgraded = True
                    time.sleep(2)
                elif sw_ver[-42:] == "Version 15.3(3)JF5, RELEASE SOFTWARE (fc2)":
                    upgraded = False
                    time.sleep(2)
                    break

            else:
                break
        if line == "ap#":
            ac_serial.write(ser, b'exit\r')
            print(ac_serial.read(ser))
        if line == 'Press RETURN to get started.':
            ac_serial.write(ser, b'\r')
        
        if line[:9] == ' --More--':
            ac_serial.write(ser, b' ')
            ac_serial.write(ser, b'\r')

        
        if line[-13:] == 'image version':
            ac_serial.write(ser, b'\r')
        
        if len(line) == 17 and line[:2] == 'AP':
            autonomous = False
            upgraded = False
            command = False
            fleet = False
            break
        elif line[-8:] == 'command#':
            autonomous = True
            upgraded = True
            command = True
            fleet = False
            break
        elif line[-6:] == 'fleet#':
            autonomous = True
            upgraded = True
            command = True
            fleet = True
            break


    ser.close()
    return(autonomous, upgraded, command, fleet)


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


def step2p5(com):
    print('Step 2.5')
    ser = ac_serial.initSerial(com)

    logged_in = False
    enable = False
    debug = False
    finished_boot = False

    for x in range(3):
        ac_serial.write(ser, b'\r')

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)

        if logged_in:
            if enable and not debug:
                ac_serial.write(ser, b'debug capwap console cli')
                time.sleep(1)
                ac_serial.write(ser, b'\n')
                debug = True

            if enable and debug:
                if line[-11:] == '(yes/[no]):':
                    ac_serial.write(ser, b'yes')
                    time.sleep(1)
                    ac_serial.write(ser, b'\n')         
                elif len(line) == 17 and line[:2] == 'AP':
                    ac_serial.write(ser, b'capwap ap autonomous')
                    line = ac_serial.read(ser)
                    print(line)
                    time.sleep(1)
                    ac_serial.write(ser, b'\n')
                    line = ac_serial.read(ser)
                    print(line)
                    ac_serial.write(ser, b'yes')
                    time.sleep(1)
                    ac_serial.write(ser, b'\n')
                    line = ac_serial.read(ser)
                    print(line)
                    break
                elif line[-1:] == '#':
                    time.sleep(1)
                    ac_serial.write(ser, b'\n')
                
            
            else:
                if len(line) == 17 and line[:2] == 'AP':
                    time.sleep(1)
                    ac_serial.write(ser, b'en')
                    line = ac_serial.read(ser)
                    print(line)
                    time.sleep(1)
                    ac_serial.write(ser, b'\n')
                    line = ac_serial.read(ser)
                    print(line)
                    time.sleep(1)

                if line[:9] == 'Password:':
                    time.sleep(1)
                    ac_serial.write(ser, b'Cisco')
                    time.sleep(0.5)
                    ac_serial.write(ser, b'\n')
                    enable = True


        else:
            if finished_boot:
                if len(line) == 17 and line[:2] == 'AP':
                    time.sleep(1)
                    ac_serial.write(ser, b'login')
                    line = ac_serial.read(ser)
                    print(line)
                    time.sleep(1)
                    ac_serial.write(ser, b'\r')
                    line = ac_serial.read(ser)
                    print(line)
                    time.sleep(3)
                    line = ac_serial.read(ser)
                    print(line)
                if line[:9] == 'Username:':
                    ac_serial.write(ser, b'cisco\r')
                    line = ac_serial.read(ser)
                    print(line)
                    time.sleep(3)
                if line[:9] == 'Password:':
                    ac_serial.write(ser, b'Cisco')
                    time.sleep(3)
                    line = ac_serial.read(ser)
                    print(line)
                    ac_serial.write(ser, b'\r')
                    line = ac_serial.read(ser)
                    print(line)   
                    logged_in = True
            else:
                print("Waiting for the bootup to complete...")
                if line[-25:] == 'Invoking capwap discovery':
                    finished_boot = True
                elif line[:2] == 'AP':
                    finished_boot = True

    return(True, False)

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
        else:
            ac_serial.write(ser, b'\r')

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
        if line[:9] == ' --More--':
            ac_serial.write(ser, b' ')
            ac_serial.write(ser, b'\r')


def step4(com):
    print('Step 4')
    ser = ac_serial.initSerial(com)


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
        
        if line == 'ap#':
            time.sleep(1)
            ac_serial.write(ser, b'archive download-sw /overwrite /force-reload tftp://10.0.0.5/ap3g2-k9w7-tar.153-3.JI1.tar')
            time.sleep(1)
            ac_serial.write(ser, b'\r')
        elif line == 'ap>':
            ac_serial.write(ser, b'en')
            ac_serial.write(ser, b'\n')
            time.sleep(1)


        elif line[:9] == 'Password:':
            time.sleep(1)
            ac_serial.write(ser, b'Cisco')
            time.sleep(0.5)
            ac_serial.write(ser, b'\n')
            enable = True

        elif line[-18:] == 'console by console':
            time.sleep(1)
            ac_serial.write(ser, b'\r')
        elif line[-22:] == 'existing image version':
            break
        elif line[:9] == ' --More--':
            ac_serial.write(ser, b' ')
            ac_serial.write(ser, b'\r')
        

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


def step6(com, vehicle):
    print('Step 6')
    ser = ac_serial.initSerial(com)

    fleet_copy = False
    command_copy = False

    for x in range(3):
        ac_serial.write(ser, b'\r')

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)
        else:
            ac_serial.write(ser, b'\r')

        if line == "ap#":
            fleet_file = 'copy tftp://10.0.0.5/cb-{}-fleet.txt flash:'.format(vehicle[0])
            fleet_b = str.encode(fleet_file)
            command_file = 'copy tftp://10.0.0.5/cb-{}-command.txt flash:'.format(vehicle[0])
            command_b = str.encode(command_file)
        

            if not fleet_copy:
                ac_serial.write(ser, fleet_b)
                line = ac_serial.read(ser)
                print(line)
                time.sleep(1)
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(3)
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(2)
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(2)
                fleet_copy = True
        
            if not command_copy:
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(1)
                ac_serial.write(ser, command_b)
                line = ac_serial.read(ser)
                print(line)
                time.sleep(1)
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(3)
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(2)
                ac_serial.write(ser, b'\r')
                line = ac_serial.read(ser)
                print(line)
                time.sleep(1)
                command_copy = True

            if fleet_copy and command_copy:
                return(True)


def step7(com, vehicle):
    print('Step 7')
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
        else:
            ac_serial.write(ser, b'\r')

        if line == 'ap#':

            load_fleet = 'copy flash:cb-{}-fleet.txt running-config'.format(vehicle[0])
            fleet_b = str.encode(load_fleet)
            load_command = 'copy flash:cb-{}-command.txt running-config'.format(vehicle[0])
            command_b = str.encode(load_command)

            ac_serial.write(ser, command_b)
            line = ac_serial.read(ser)
            print(line)
            time.sleep(1)
            ac_serial.write(ser, b'\r')
            line = ac_serial.read(ser)
            print(line)
            time.sleep(1)
            ac_serial.write(ser, b'\r')
            line = ac_serial.read(ser)
            print(line)
            time.sleep(1)

        if line[-8:] == 'command#':
            print("Command config loaded")
            break
    return(True)

def step8(com):
    print('Step 8')
    ser = ac_serial.initSerial(com)

    ping = False

    for x in range(3):
        ac_serial.write(ser, b'\r')

    while True:
        try:
            line = ac_serial.read(ser)
        except:
            pass

        if line:
            print(line)
        else:
            ac_serial.write(ser, b'\r')

        if line[-8:] == 'command#':
            if not ping:
                ac_serial.write(ser, b'ping 10.221.64.1\r')
                for x in range(5):
                    line = ac_serial.read(ser)
                    print(line)
                    if line[:7] == 'Success' or line[:1] == '!':
                        return(True)
                    else:
                        pass


def step9(com, vehicle):
    print('Step 7')
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
        else:
            ac_serial.write(ser, b'\r')

        if line[-8:] == 'command#':

            load_fleet = 'copy flash:cb-{}-fleet.txt running-config'.format(vehicle[0])
            fleet_b = str.encode(load_fleet)
            load_command = 'copy flash:cb-{}-command.txt running-config'.format(vehicle[0])
            command_b = str.encode(load_command)

            ac_serial.write(ser, fleet_b)
            line = ac_serial.read(ser)
            print(line)
            time.sleep(1)
            ac_serial.write(ser, b'\r')
            line = ac_serial.read(ser)
            print(line)
            time.sleep(1)
            ac_serial.write(ser, b'\r')
            line = ac_serial.read(ser)
            print(line)
            time.sleep(1)

        if line[-6:] == 'fleet#':
            print("Fleet config loaded")
            return(True)

def step10(com):
    print('Step 10')
    ser = ac_serial.initSerial(com)

    for x in range(3):
        ac_serial.write(ser, b'\r')
        line = ac_serial.read(ser)

    if line[-6:] == 'fleet#':
        print("Fleet config loaded")
        ac_serial.write(ser, b'wr mem\r')
        line = ac_serial.read(ser)
        print(line)
        time.sleep(1)
        ac_serial.write(ser, b'\r')
        line = ac_serial.read(ser)
        print(line)
        time.sleep(1)
        return(True)


def main():
    print("WARNING: This script is SUPER buggy, always verify after use")
    time.sleep(3)
    com = ac_com.get()
    configs = False
    vehicle = False
    ping = False
    fleet = False
    complete = False

    vehicle = step0()
    autonomous, upgraded, command, fleet = step1(com)

    if not complete:
        while True:
            if command and not fleet:
                configs = True
                ping = step8(com)
            elif fleet and command:
                configs = True
                ping = True
                complete = step10(com)

            elif autonomous and upgraded:
                if not command:
                    print('In autonomous')
                    print('Upgraded')
                    step5(com)
                elif command:
                    ping = step8(com)
            elif autonomous and not upgraded:
                print("Autonomous")
                print("Not upgraded")
                step3(com)
                print("IP Set")
                step4(com)
                upgraded = True
            elif not autonomous and not upgraded:
                print("Not autonomous")
                print("Not upgraded")
                autonomous, upgraded = step2p5(com)
                step3(com)
                print("IP Set")
                step4(com)
                upgraded = True

            

            if vehicle and not configs:
                if not command and not configs:
                    step5(com)
                    configs = step6(com, vehicle)
                    command = step7(com, vehicle)
            elif not vehicle and not configs:
                step4(com)
            elif vehicle and configs:
                if not command:
                    command = step7(com, vehicle)

            
            if command and not ping:
                ping = step8(com)
            elif command and ping:
                if not fleet and not complete:
                    fleet = step9(com, vehicle)
                    complete = step10(com)
            
            if fleet and not complete:
                complete = step10(com)
            elif fleet and complete:
                print('HOLY FUCK made it to the end')
                print('----------------------------')
                print('   VEHICLE: {}'.format(vehicle[0]))
                print('  FLEET IP: {}'.format(vehicle[2]))
                print('COMMAND IP: {}'.format(vehicle[1]))
                print('----------------------------')
                break

    elif complete:
        print('HOLY FUCK made it to the end')
        print('----------------------------')
        print('   VEHICLE: {}'.format(vehicle[0]))
        print('  FLEET IP: {}'.format(vehicle[2]))
        print('COMMAND IP: {}'.format(vehicle[1]))
        print('----------------------------')

if __name__ == "__main__":
    main()