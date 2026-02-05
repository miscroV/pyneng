# -*- coding: utf-8 -*-
"""
Task 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), print to the stdout:
    'unicast' - if the first byte is in the range 1-223
    'multicast' - if the first byte is in the range 224-239
    'local broadcast' - if the IP address is 255.255.255.255
    'unassigned' - if the IP address is 0.0.0.0
    'unused' - in all other cases

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip_list = list(map(int, input("ip: ").split(".")))
if 1 <= ip_list[0] <= 223:
    ip_type = "unicast"
elif 222 <= ip_list[0] <= 239:
    ip_type = "multicast"
elif all([x == 255 for x in ip_list]):
    ip_type = "local broadcast"
elif all([x == 0 for x in ip_list]):
    ip_type = "unassigned"
else:
    ip_type = "unused"
print(ip_type)