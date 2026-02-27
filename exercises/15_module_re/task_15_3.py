# -*- coding: utf-8 -*-
"""
Task 15.3

Create a convert_ios_nat_to_asa function that converts NAT rules from
cisco IOS syntax to cisco ASA.

The function expects such arguments:
- the name of the file containing the Cisco IOS NAT rules
- the name of the file in which to write the NAT rules for the ASA

The function returns None.

Check the function on the cisco_nat_config.txt file.

Example cisco IOS NAT rules
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

And the corresponding NAT rules for the ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

In the file with the rules for the ASA:
- there should be no blank lines between the rules
- there must be no spaces before the lines "object network"
- there must be one space before the rest of the lines

In all rules for ASA, the interfaces will be the same (inside, outside).
"""

import re

def convert_ios_nat_to_asa(ios_nat_rules_file: str, asa_nat_rules_file: str) -> None:
    """
    convert cisco ios nat rules from ios_nat_rules_file into asa style rules and write to asa_nat_rules_file.
    
    :param ios_nat_rules_file: file path for ios nat rules to convert
    :type ios_nat_rules_file: str
    :param asa_nat_rules_file: file path to write asa nat rules to. 
    :type asa_nat_rules_file: str
    """
    asa_format = ["object network LOCAL_{}",
                  " host {}",
                  " nat (inside,outside) static interface service tcp {} {}"]
    nat_reader: re.Pattern[str] = re.compile(r'(?:\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+)'
                                             r'(?P<ip>\S+)\s+'
                                             r'(?P<port>\d+)\s+'
                                             r'(?:\S+\s+\S+\s+)'
                                             r'(?P<externalPort>\d+)\s+'
                                             )
    with open(ios_nat_rules_file, 'r') as ios, open(asa_nat_rules_file, 'w') as asa:
        #! a list of tuples in the form 'ip', 'internal port', 'external port'
        nat_configs = nat_reader.findall(ios.read())
        for ip, i_port, e_port in nat_configs:
            print("\n".join(asa_format).format(ip, ip, i_port, e_port), file=asa)


convert_ios_nat_to_asa(
    "/workspaces/pyneng/exercises/15_module_re/cisco_nat_config.txt", 
    "/workspaces/pyneng/exercises/15_module_re/cisco_asa_nat_config.test"
    )
