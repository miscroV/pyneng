# -*- coding: utf-8 -*-
"""
Task 7.3b

Make a copy of the code from the task 7.3a.

Add this functionality:
- Ask the user to enter the VLAN number.
- Print information only for the specified VLAN.

Output example:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
import re
cam_file = "CAM_table.txt"
mac_re = r"([0-9a-fA-F]{4}[.]){2}[0-9a-fA-F]{4}"

selected_vlan = input("Enter VLAN number: ")

with open(cam_file, 'r') as f:
    mac_list = []
    for line in f:
        if not re.search(mac_re, line):
            continue;
        vlan,mac,_,port = line.split()
        mac_list.append((vlan,mac,port))

vlan_sorted = sorted(mac_list, key=lambda mac: (int(mac[0]), mac[1]))
for vlan,mac,port in vlan_sorted:
    if not vlan == selected_vlan:
        continue
    print(f"{vlan.ljust(9)}{mac.ljust(20)}{port.ljust(6)}")