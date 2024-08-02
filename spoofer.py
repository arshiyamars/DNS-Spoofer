#!/usr/bin/python3
import scapy.all as scapy


Ip = input("Enter IP : ")

# Find MAC by IP
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_rq_broadcast = broadcast / arp_request
    answer_list = scapy.srp(arp_rq_broadcast, timeout=1, verbose=False)[0]
    print(answer_list[0][1].hwsrc)

get_mac(Ip)
