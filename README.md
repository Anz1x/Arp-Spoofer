# Arp-Spoofer
Arp spoofer made in Python 3.10.2.

https://user-images.githubusercontent.com/50573902/159108653-a8f31d27-d0dd-4ee0-a87d-d2e714994bac.mp4

DISCLAIMER:

- I am not responsible with your illegal intentions with this so don't use this on someone explicitly without their permission.

Third Party Modules:

- scapy
- colorama

Installation:

1. Just clone this or download this as a zip:

- git clone https://github.com/Anz1x/Arp-Spoofer

2. Install all the necessary modules in order for this arp spoofer to run

- pip3 install -r requirements.txt

3. Give execution permissions

- chmod +x arpspoofer.py

Usage:

1. In order to use this you first need to run the file and specify 2 arguments: the router and the target (in order)

- ./arpspoofer.py <router_ip> <target_ip>

- EXAMPLE: ./arpspoofer.py 192.168.1.1 192.168.1.254


![image](https://user-images.githubusercontent.com/50573902/159108132-33cea26c-e60d-4333-84ad-88165c1b0ed2.png)

2. (OPTIONAL) after you run the arp spoofer you may notice that the target may not be able to connect to the internet or it might be slow since it's sending malicious packets to the target so if you want the target to use the internet normally just type this before you run the program:

- echo 1 >> /proc/sys/net/ipv4/ip_forward

3. The program is running on an infinite while loop so it won't stop by itself so if you want to stop the program just use the keyboard shortcut ctrl + c
