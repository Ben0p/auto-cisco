import serial
import time
from commands import com

def open(com_port):
    print("Initializing {}...".format(com_port))

    while True:
        try:
            console = serial.Serial(
                port=com_port,
                baudrate=9600,
                parity="N",
                stopbits=1,
                bytesize=8,
                timeout=1
            )

            return(console)

        except:
            print("Incorrect serial port, or port is in use.")
            print("Is putty open?")
            input("Press ENTER to try again...")
    
def port():
    com_port = com.get()
    console = open(com_port)
    return(console)
