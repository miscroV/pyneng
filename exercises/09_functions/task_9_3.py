# -*- coding: utf-8 -*-
"""
Task 9.3

Create a get_int_vlan_map function that handles the switch configuration
file and returns a tuple of two dictionaries:

* a dictionary of ports in access mode, where the keys are port numbers,
  and the access VLAN values (numbers):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* a dictionary of ports in trunk mode, where the keys are port numbers,
  and the values are the list of allowed VLANs (list of numbers):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

The function must have one parameter, config_filename, which expects as an argument
the name of the configuration file.

Check the operation of the function using the config_sw1.txt file.

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