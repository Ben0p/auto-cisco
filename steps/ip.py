from netifaces import interfaces, ifaddresses, AF_INET
import socket

def get():
    print("Getting local IPs and hostname...")
    ip_list = []
    for interface in interfaces():
        for link in ifaddresses(interface)[AF_INET]:
            ip_list.append(link['addr'])

    hostname = socket.gethostname()
    print("Hostname: {}".format(hostname))
    print("IPs: {}".format(ip_list))
    return(hostname, ip_list)

if __name__ == '__main__':
    get()