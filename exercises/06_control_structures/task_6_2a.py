# -*- coding: utf-8 -*-
"""
Task 6.2a

Make a copy of the code from the task 6.2.

Add verification of the entered IP address.
An IP address is considered correct if it:
    - consists of 4 numbers (not letters or other symbols)
    - numbers are separated by a dot
    - every number in the range from 0 to 255

If the IP address is incorrect, print the message: 'Invalid IP address'

The message "Invalid IP address" should be printed only once,
even if several points above are not met.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
try:
    ip_list = list(map(int, input("ip: ").split(".")))
    if ((len(ip_list) != 4) or not all([0 <= o <= 255 for o in ip_list])):
        raise ValueError("Invalid IP address")
except ValueError:
    print("Invalid IP Address")
else:
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
