import serial
import time

'''
Auto Cisco serial module
'''


def initSerial(com):
    return(serial.Serial(com,9600,timeout=1.5))

def read(ser):
    return(ser.readline().decode("utf-8").rstrip("\n\r"))

def write(ser, command):
    ser.write(command)



if __name__ == '__main__':
    init_serial('COM6')
    while True:
        print(Stream.data())