Overview

This exercise focused on creating a SYN flood attack using Python and Scapy. The script sends 100 SYN packets to 10 selected IP addresses while spoofing the source IP address. Additionally, it uses at least 10 different source ports for the TCP packets.


Conclusion

After I formualted the script, I ran a test. As I did that I used wireshark to capture the traffic, which recorded the 100 SYN packets for the designated ip address, confirming the syn flood. The pcap file is present in the same folder with the name: syn_floof_test.pcap


