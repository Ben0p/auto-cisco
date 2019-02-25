import time

def serial(console):
    '''
    Check if there is data waiting to be read
    Read and return it.
    else return null string
    '''
    buffer = console.inWaiting()
    if buffer:
        lines = console.read(buffer)
        lines = lines.decode('ascii')
        lines = lines.replace('\x08', '')
        lines = lines.strip()
        lines = lines.splitlines()
        if lines:
            for line in lines:
                print(line)
            return(lines)
        else:
            return('')