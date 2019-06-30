from netifaces import interfaces, ifaddresses, AF_INET
import socket

def get():
    print("Getting local IPs and hostname...")
    ip_list = []
    for interface in interfaces():
        try:
            addresses = ifaddresses(interface)[AF_INET]
        except:
            addresses = []
        if len(addresses) > 0:
            for link in addresses:
                if 'addr' in link:
                    ip_list.append(link['addr'])
        else:
            ip_list.append('')

    hostname = socket.gethostname()
    print("Hostname: {}".format(hostname))
    print("IPs: {}".format(ip_list))
    return(hostname, ip_list)

if __name__ == '__main__':
    get()