# -*- coding: utf-8 -*-
"""
Task 9.3a

Make a copy of the code from the task 9.3.

Add this functionality: add support for configuration when the port is in VLAN 1
and the access port setting looks like this:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

In this case, information should be added to the dictionary that the port in VLAN 1
Dictionary example:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw2.txt file.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
def get_int_vlan_map(config_filename):
    access_intfs = {}
    trunk_intfs  = {}

    intf, vlans, is_access = None, None, None
    with open(config_filename, 'r') as file:
        for line in file:

            if "interface" in line: 
                intf = line.split()[1]
                continue
            
            if "access" in line:
                is_access = True
                
            if "vlan" in line:
                vlans = list(map(int,line.split()[-1].split(",")))
            else: continue

            if is_access:
                access_intfs[intf] = vlans[0]
            else:
                trunk_intfs[intf] = vlans

            intf, vlans, is_access = None, None, None

    return (access_intfs, trunk_intfs)

print(get_int_vlan_map("config_sw1.txt"))