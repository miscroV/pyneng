# -*- coding: utf-8 -*-
"""
Task 15.2

Create a function parse_sh_ip_int_br that expects as an argument the name
of the file containing the output of the show ip int br command.

The function should process the output of the show ip int br command
and return the following fields:
* Interface
* IP-Address
* Status
* Protocol

The information should be returned as a list of tuples:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

To get this result, use regular expressions.

Check the operation of the function using the example of the sh_ip_int_br.txt file.

"""
import re

def parse_sh_ip_int_br(file_name) -> list[tuple]:
    ip_int_b_re = re.compile(
        r'(?P<intf>\S+) \s+'           # Interface
        r'(?P<ip>\S+) \s+'             # IP Address
        r'(?:\S+)\s+'                     # OK? (skipped)
        r'(?:\S+)\s+'                     # Method (skipped)
        r'(?P<status>(?:up|down|administratively down))\s+'      # Status (captures "admin down" via non-greedy + spacing)
        r'(?P<protocol>(?:up|down|administratively down))\s+'          # Protocol
    )
    
    
    with open(file_name) as file:
        return ip_int_b_re.findall(file.read())

if __name__ == '__main__':
    print(parse_sh_ip_int_br('/workspaces/pyneng/exercises/15_module_re/sh_ip_int_br.txt'))