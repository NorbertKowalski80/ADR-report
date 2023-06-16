import platform
import os
from datetime import datetime

def arp_table_extraction():
    system = platform.system()
    if system == "Windows":
        return arp_table_extraction_windows()
    elif system == "Linux":
        return arp_table_extraction_linux()
    else:
        print("Platform is not supported!")
        exit()

def arp_table_extraction_windows():
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    addresses = {}
    for line in arp_table_lines:
        if not line:
            continue
        line = " ".join(line.split())
        line_splitted = line.split()
        if "Interface" in line_splitted[0]:
            interface = line_splitted[3]
            continue
        if 'Internet' in line_splitted[0]:
            continue
        if line_splitted[2] == "static":
            continue
        addresses[line_splitted[0]] = [line_splitted[1], interface]
    return addresses

def arp_table_extraction_linux():
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    addresses = {}
    for line in arp_table_lines:
        if not line:
            continue
        line = " ".join(line.split())
        line_splitted = line.split()
        addresses[line_splitted[1].replace("(", "").replace(")", "")] = [line_splitted[3], line_splitted[6]]
    return addresses

def create_log(message):
    print("Generating logs...")
    with open('log.txt', "a") as log:
        log.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " " + message + "\n")

def identify_duplication(addresses):
    tmp_mac_list = []
    spoof_found = False
    print("Scanning...")
    for mac in addresses.values():
        if mac in tmp_mac_list:
            create_log("ARP Spoofed! The address is: " + mac[0] + " on interface " + mac[1])
            spoof_found = True
        else:
            tmp_mac_list.append(mac)
    if not spoof_found:
        create_log("ARP Spoofing has not been found")
    print("Scanning Finished")

if __name__ == "__main__":
    identify_duplication(arp_table_extraction())