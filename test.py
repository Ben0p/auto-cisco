import serial

ser = serial.serial_for_url('loop://', timeout=1)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

sio.write("hello\n")
sio.flush() # it is buffering. required to get the data out *now*
hello = sio.readline()
print(hello == "hello\n")
print(hello.replace('\n', ''))