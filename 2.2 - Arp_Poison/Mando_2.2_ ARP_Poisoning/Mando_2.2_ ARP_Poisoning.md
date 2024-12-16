
### <a name="_g1iq6rdoe1nu"></a>**Overview**
This exercise aimed to perform a Man-in-the-Middle (MitM) attack using ARP poisoning, and capture HTTP traffic. 

Bonus: Bypass browser security warnings by creating and deploying a fake certificate.
### <a name="_rgkvxll2j842"></a>**Steps to Perform ARP Poisoning and MitM**
#### <a name="_r2fxpmk6fe8y"></a>**1. Create ARP Poisoning Script**
By using scapy, I created the script arp\_poisoning.py

**Script Summary:**

- Target IP: 172.16.4.132
- Router IP: Determined dynamically or set to 172.16.4.2
- Spoofed MAC: Attacker's MAC address (00:0c:29:10:09:c3)
- Packets sent continuously to poison ARP caches of both target and router.
#### <a name="_qv3nf73qnzsa"></a>**2. Setup IP tables Rules**
- IP tablez rules were configured to redirect traffic to specific ports for processing:
- And it was made sure that HTTP requests sent to Kali do not end up in the preroute rule:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.001.png)

- Port forwarding enabled:

  ![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.002.png)![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.003.png)


#### <a name="_prjoqugmidcj"></a>**3. Prepare Directories**
Created directories for storing logs and sniffed data:

sudo mkdir /tmp/sslsplit

sudo mkdir /home/kali/Documents/network\_security/Mandatory\_II/arp\_poisoning/sniff\_data

sudo mkdir /home/kali/Documents/network\_security/Mandatory\_II/arp\_poisoning/logs
#### <a name="_a4e7zgr64mt4"></a>**4. Run SSLsplit**
SSLsplit was used to intercept and log HTTPS traffic:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.004.png)
#### <a name="_pl78tpqy85zs"></a>**5. Run arp\_poisoning.py script**
![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.005.png)

#### <a name="_9xs451sgdlgw"></a>**6. Test Browser Behavior**
On the target machine:

- Visited kea.dk in Firefox.
- Observed a security warning regarding an untrusted certificate.
- Verified the certificate matched the one created.

Firefox gives an alert:![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.006.png)

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.007.png)

` `When the certificate is checked, it is the one I created:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.008.png)


In the target machine, when **arp -a** is checked, default gateway has become kali linux:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.009.png)









When I accept the security risk and continue, I can reach kea.dk but connection is not secure:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.010.png)
#### <a name="_x9pu9aovdsi5"></a>**7. Generate SSL Certificate**
A self-signed certificate was created for HTTPS interception:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.011.png)

Certificate saved to: /home/kali/Documents/network\_security/Mandatory\_II/arp\_poisoning/mitm\_certs/

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.012.png)

#### <a name="_at8u3h7yahd3"></a>**8. Deploy Certificate to Target Machine**
To bypass the browser warning:

1. Transferred the certificate:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.013.png)

1. Installed the certificate as a trusted authority:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.014.png)

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.015.png)

1. Converted to PEM format for Firefox:

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.016.png)

1. Imported the certificate into Firefox:![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.017.png)

![](Aspose.Words.88965f62-5a01-4f56-bb76-45c4e6bcab5e.018.png)
#### <a name="_in2qqiwxcaa4"></a>**8. Re-Test Browser Behavior**
After importing the PEM certificate into Firefox, I re-tested kea.dk. But this time arp spoofing did not succeed for reasons I couldn’t figure out. 

It could be that I have used the target machine to test other tools for System Security class exercises, in which I have installed tools like portsentry, squid and played around with iptables. I uninstalled these and tried again, but it still couldn’t spoof the ip. 
### <a name="_7irolbhbzzpc"></a>**Conclusion**
- The setup was configured correctly, and it worked. But the browser could detect the spoofing.
- Fake certificate created and imported successfully. But this time, arp spoof didn’t work even though I tried different troubleshooting methods.


