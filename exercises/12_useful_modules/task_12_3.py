# -*- coding: utf-8 -*-
"""
Task 12.3

Create a function print_ip_table that prints a table of available
and unavailable IP addresses.

The function expects two lists as arguments:
* list of available IP addresses
* list of unavailable IP addresses

The result of the function is printing a table to the stdout:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""


def print_ip_table(available_ips, unavailable_ips):
    IPTable = [
        "Reachable    Unreachable",
        "-----------  -------------"
    ]
    for i in range(max(len(available_ips), len(unavailable_ips))):
        try:    r =  available_ips[i]
        except: r = ""
        try:    un_r = unavailable_ips[i]
        except: un_r = ""
        IPTable.append(f"{r:<13}{un_r}")

    print("\n".join(IPTable))

if __name__ == "__main__":
    print_ip_table(['10.1.1.1'], ["10.3.3.3", "10.3.4.3"])