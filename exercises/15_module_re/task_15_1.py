# -*- coding: utf-8 -*-
"""
Task 15.1

Create a get_ip_from_cfg function that expects the name of the file containing
the device configuration as an argument.

The function should process the configuration and return the IP addresses and
masks that are configured on the interfaces as a list of tuples:
* the first element of the tuple is the IP address
* the second element of the tuple is a mask

For example (arbitrary addresses are taken):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

To get this result, use regular expressions.

Check the operation of the function using the config_r1.txt file.

Please note that in this case, you can not check the correctness
of the IP address, address ranges, and so on, since the command
output from network device is processed, not user input.

"""
import re

def get_ip_from_cfg(file_name: str) -> list[tuple]:
    reg = re.compile(r'interface.*'
                     r'?ip address (?P<ip>\b(?:\d{1,3}\.){3}\d{1,3}\b) '
                     r'(?P<netmask>\b(?:\d{1,3}\.){3}\d{1,3}\b)'
                     r'', 
                     re.DOTALL | re.MULTILINE)
    ip_list = []
    with open(file_name) as file:
        for match in reg.finditer(file.read()):
          ip_list.append((match['ip'], match['netmask']))
    return ip_list

if __name__ == '__main__':
    print(get_ip_from_cfg('/workspaces/pyneng/exercises/15_module_re/config_r1.txt'))