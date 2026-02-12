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

            # get the interface
            if "interface" in line: 
                intf = line.split()[1]
                continue
            
            # get access and set default vlan before next line.
            if "access" in line and "vlan" not in line:
                is_access = True
                vlans = [1]
                continue

            # if alternate vlans found set the vlans,
            if "vlan" in line:
                vlans = list(map(int,line.split()[-1].split(",")))
                
            # if vlans is set, continue the loop, otherwise continue until vlans are found. 
            elif vlans: pass
            else: continue

            if is_access:
                access_intfs[intf] = vlans[0]
            else:
                trunk_intfs[intf] = vlans

            intf, vlans, is_access = None, None, None

    return (access_intfs, trunk_intfs)

print(get_int_vlan_map("config_sw1.txt"))