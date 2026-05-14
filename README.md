# Project-ARP-Cache-Poisoning-Attack

## Objective
The goal of this project is to perform a series of Man-in-the-Middle (MITM) attacks using ARP cache poisoning. I demonstrated how to redirect traffic between a client and server through an attacker machine to intercept and modify data in real-time.

## Tools & Environment
* **Language:** Python (Scapy library)
* **Environment:** SEED Labs (Ubuntu VMs)
* **Tools:** Wireshark, Telnet, Netcat

## Project Phases

### Phase 1: ARP Poisoning Techniques
I developed Python scripts to poison the ARP cache of a target host using three different methods:
1.  **ARP Request Spoofing:** Sending a spoofed request to update the victim's cache.
2.  **ARP Reply Spoofing:** Sending unsolicited replies (noting that modern systems only accept these if an entry already exists).
3.  **Gratuitous ARP:** Using broadcast packets to announce a mapping.

### Phase 2: Telnet MITM Attack
After poisoning the ARP caches of both the client and server to redirect traffic through my machine, I used a sniffing-and-spoofing script to:
* Intercept Telnet traffic.
* Modify the payload in real-time (e.g., replacing all typed characters with 'Z').
* **Result:** Successfully hijacked the session, making the terminal unusable for the victim.

### Phase 3: Netcat TCP Modification
I extended the MITM attack to a Netcat TCP connection. The challenge here was modifying the payload while maintaining the correct TCP sequence numbers to prevent the connection from dropping.
* **Attack:** Automatically replaced specific strings (like my name) with a placeholder string.

## Key Takeaways
* Demonstrated the vulnerability of the ARP protocol.
* Gained experience with packet manipulation and sniffing using Scapy.
* Understood the importance of IP forwarding and TCP sequence integrity in network attacks.