import tftpy


def start():
    server = tftpy.TftpServer('')
    server.listen('0.0.0.0', 69)


if __name__ == '__main__':
    import os
    os.chdir('..')
    start()