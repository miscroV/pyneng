# -*- coding: utf-8 -*-
"""
Task 7.1

Process the lines from the ospf.txt file and print information for each line
in this form to the stdout:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""

ospf_long_format = "\
Prefix                {} \n\
AD/Metric             {} \n\
Next-Hop              {} \n\
Last update           {} \n\
Outbound Interface    {}"

with open('ospf.txt', 'r') as f:
    for line in f:
        _,pref,met,_,nHop,lUpdate,oInt,*_ = line.split()
        met, nHop, lUpdate = met[1:-1], nHop[:-1], lUpdate[:-1] # clean formatting of select items
        print(ospf_long_format.format(pref,met,nHop,lUpdate,oInt))