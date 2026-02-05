# -*- coding: utf-8 -*-
"""
Task 7.2b

Make a copy of the code from the task 7.2a.
Add this functionality: instead of printing to stdout,
the script should write the resulting lines to a file.

File names must be passed as arguments to the script:
  1. name of the source configuration file
  2. name of the destination configuration file

In this case, the lines that are contained in the ignore list and lines
that start with ! must be filtered.

Restriction: All tasks must be done using the topics covered in this and previous chapters.

"""
from sys import argv
ignore = ["duplex", "alias", "configuration"]
source_config_file = argv[1]
dest_config_file = argv[2]

with open(source_config_file, 'r') as rf, open(dest_config_file,'w') as wf:
    for line in rf:
        if line[0] == "!": continue
        if any([i in line for i in ignore]): continue
        wf.write(line)