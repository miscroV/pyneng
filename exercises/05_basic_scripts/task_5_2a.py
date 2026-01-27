# -*- coding: utf-8 -*-
"""
Task 5.2a

Copy and modify the script from task 5.2 so that, if the user entered a host address
rather than a network address, convert the host address to a network address
and print the network address and mask, as in task 5.2.

An example of a network address (all host bits are equal to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address example:
* 10.0.1.1/24 - host from network 10.0.1.0/24
* 10.0.5.195/28 - host from network 10.0.5.192/28

If the user entered the address 10.0.1.1/24, the output should look like this:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Check the script work on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

Hint:
The network address can be calculated from the binary host address and the netmask.
If the mask is 28, then the network address is the first 28 bits host addresses + 4 zeros.
For example, the host address 10.1.1.195/28 in binary will be:
bin_ip = "00001010000000010000000111000011"

Then the network address will be the first 28 characters from bin_ip + 0000
(4 because in total there can be 32 bits in the address, and 32 - 28 = 4)
00001010000000010000000111000000

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
ip_net, ip_mask = input("Input network in CIDR format: ").split("/")
ip_mask = int(ip_mask)

# Input verification would go here.
 
ip_list          = [c for c in ip_net.split(".")]
bin_ip_list      = [bin(int(c))[2:] for c in ip_list]

bin_ip_mask_list = [("1" * ip_mask + "0" * (32 - ip_mask))[c:c+8] for c in range(0,32,8) ]
ip_mask_list     = [str(int(c, 2)) for c in bin_ip_mask_list]
1
net_ip_list      = [ int(ip, 2) & int(mask, 2) for ip, mask in zip(bin_ip_list, bin_ip_mask_list)]
bin_net_ip_list      = [bin(int(c))[2:] for c in net_ip_list]

print("\n".join([
    "Network: ",
    f"{net_ip_list[0]:8}  {net_ip_list[1]:8}  {net_ip_list[2]:8}  {net_ip_list[3]:8}",
    f"{bin_net_ip_list[0]:0>8}  {bin_net_ip_list[1]:0>8}  {bin_net_ip_list[2]:0>8}  {bin_net_ip_list[3]:0>8}",
    "",
    "Mask: ",
    f"/{ip_mask}",
    f"{ip_mask_list[0]:8}  {ip_mask_list[1]:8}  {ip_mask_list[2]:8}  {ip_mask_list[3]:8}",
    f"{bin_ip_mask_list[0]:0>8}  {bin_ip_mask_list[1]:0>8}  {bin_ip_mask_list[2]:0>8}  {bin_ip_mask_list[3]:0>8}",
    ]))