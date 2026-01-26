# -*- coding: utf-8 -*-
"""
Task 5.2

Ask the user to enter the IP network in the format: 10.1.1.0/24

Then print information about the network and mask in this format:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different net/mask combinations.

Hint: You can get the mask in binary format like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

You can then take 8 bits of the binary mask using slices and convert them to decimal.

Restriction: All tasks must be done using the topics covered in this and previous chapters.
"""

ip_net, ip_mask = input("Input network in CIDR format: ").split("/")
ip_mask = int(ip_mask)

# Input verification would go here.

ip_list = [c for c in ip_net.split(".")]
ip_mask_list = [str(int(c, 2)) for c in bin_ip_mask_list]

bin_ip_mask_list = [ ("1" * ip_mask + "0" * (32 - ip_mask))[c:c+8] for c in range(0,32,8) ]
bin_ip_list = [bin(int(c))[2:] for c in ip_list]

print("\n".join([
    "Network: ",
    f"{ip_list[0]:8}  {ip_list[1]:8}  {ip_list[2]:8}  {ip_list[3]:8}",
    f"{bin_ip_list[0]:0>8}  {bin_ip_list[1]:0>8}  {bin_ip_list[2]:0>8}  {bin_ip_list[3]:0>8}",
    "",
    "Mask: ",
    f"/{ip_mask}",
    f"{ip_mask_list[0]:8}  {ip_mask_list[1]:8}  {ip_mask_list[2]:8}  {ip_mask_list[3]:8}",
    f"{bin_ip_mask_list[0]:0>8}  {bin_ip_mask_list[1]:0>8}  {bin_ip_mask_list[2]:0>8}  {bin_ip_mask_list[3]:0>8}",
    ]))

