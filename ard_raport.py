import os
from datetime import datetime

def arp_table_exct():
    arp_table = os.popen("arp -a").read()
    arp_teble_lines = arp_table.splitlines()
    addresses = {}
    for line in arp_teble_lines:
        if "Interface" in line or "Internet" in line:
            continue
        if "ff-ff-ff-ff-ff-ff" in line or "ff:ff:ff:ff:ff:ff" in line:
            continue
        if arp_teble_lines.index(line) >= 2:
            Ip, Mac, Type = line.split()
            addresses[Ip] = Mac
        print(addresses)
        duplicate(addresses)

def duplicate(addresses):
    temp_mac = []
    mitm_macs = []
    for Mac in addresses.values():
#        print(f"before: {mac}")
        if not Mac in temp_mac:
            temp_mac.append(Mac)
        if not Mac in mitm_macs:
            mitm_macs.append(Mac)
        else:
            print(mitm_macs)
            create_log(Mac)
#        if mac in temp_mac:
#            print(f"after: {mac}")
#            mitm_macs.append(mac)
#        temp_mac.append(mac)
#        print(mitm_macs)

def create_log(msg):
    date = datetime.now()
    with open("mitm.log.txt","a") as log:
        log.write(f"{msg}  date: {date} - under attack!!!\n")

arp_table_exct()
