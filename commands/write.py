import time


def serial(console, data):
    encoded = data.encode('utf-8')
    console.write(encoded)
    time.sleep(0.5)