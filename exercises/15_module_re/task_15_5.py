# -*- coding: utf-8 -*-
"""
Task 15.5

Create a generate_description_from_cdp function that expects as an argument
the name of the file that contains the output of the show cdp neighbors command.

The function should process the show cdp neighbors command output and generate
a description for the interfaces based on the command output.

For example, if R1 has the following command output:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

For the Eth 0/0 interface, you need to generate the following description:
description Connected to SW1 port Eth 0/1

The function must return a dictionary, in which the keys are the names
of the interfaces, and the values are the command specifying the description
of the interface:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'

Check the operation of the function on the sh_cdp_n_sw1.txt file.
"""


import re
def generate_description_from_cdp(cdp_file: str) -> dict:
    cdp_reg = re.compile(r'^(?P<device_id>\S+)\s+(?P<local_interface>\S+\s\S+)\s+(?P<hold_time>\d+)\s+(?P<capabilities>(\S ){0,3})\s+(?P<platform>\S+)\s+(?P<port_id>\S+\s\S+)'
)
    ignore = ["show", "Capability", "I - IGMP"]

    descriptions = {}
    with open(cdp_file) as file:
        for row in file:
            if any([i in row for i in ignore]): 
                continue
            cdp_row = cdp_reg.search(row)
            if not cdp_row:
                continue
            descriptions.update({cdp_row['local_interface'] : f"description Connected to {cdp_row['device_id']} port {cdp_row['port_id']}"})
    return descriptions

temp = generate_description_from_cdp("/workspaces/pyneng/exercises/15_module_re/sh_cdp_n_sw1.txt")
print(temp)