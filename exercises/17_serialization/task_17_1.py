# -*- coding: utf-8 -*-
"""
Task 17.1

Create the write_dhcp_snooping_to_csv function, which processes the output
of the show dhcp snooping binding command from different files and writes
the processed data to the csv file.

Function arguments:
* filenames - list of filenames with "show dhcp snooping binding" command output
* output - the name of the csv file into which the result will be written

The function returns None.

For example, if a list with one file sw3_dhcp_snooping.txt was passed as an argument:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

The resulting csv file should contain the following content:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

The first column in the csv file, the name of the switch, must be obtained from
the file name, the rest - from the contents in the files.

Check the function on the contents of the files sw1_dhcp_snooping.txt,
sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
"""
import csv, re, os
from typing import Generator

def write_dhcp_snooping_to_csv(files: list[str], outFile: str) -> None:
    pattern = re.compile(r'(?P<mac>(?:[0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2})\s+(?P<ip>\d+.\d+.\d+.\d+)\s+(?:\d+)\s+(?:\S+)\s+(?P<vlan>\d+)\s+(?P<intf>\S+)')
    headers = ['switch', 'mac', 'ip', 'vlan', 'interface']
    device_name_splitter = '_'

    def _iter_bindings(filename: str) -> Generator[list[str], None, None]:
        switch_name = os.path.basename(filename).split(device_name_splitter)[0]
        with open(filename, 'r') as fh:
            for line in fh:
                match = pattern.search(line)
                if not match: continue
                yield [switch_name] + list(match.groups())

    with open(outFile, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for filename in files:
            for row in _iter_bindings(filename):
                writer.writerow(row)

if __name__ == '__main__':
    root_dir = '/workspaces/pyneng/exercises/17_serialization/'
    files = [root_dir + f for f in ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']]
    outfile = root_dir + 'dhcp_snooping.csv'
    write_dhcp_snooping_to_csv(files, outfile)