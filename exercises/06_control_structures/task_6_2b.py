# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the code from the task 6.2a.

Add this functionality: If the address was entered incorrectly, request the address again.

The message "Invalid IP address" should be printed only once,
even if several chacks are not passed.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""
#while True:

try:
    ip_list = list(map(int, input("ip: ").split(".")))
    if ((len(ip_list) != 4) or not all([0 <= o <= 255 for o in ip_list])):
        raise ValueError()
except ValueError:
    print("invalid ip address")
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