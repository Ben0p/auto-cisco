import tftpy

print("Running...")
server = tftpy.TftpServer('')
server.listen('0.0.0.0', 69)
