import csv
import os
import subprocess
import sys
import json
#
"""
 python module OS 
    - deal with operating system
    - filesystem operations
    - environment variables

 python module sys
    - runtime specific features
     - Data that is needed when the python file is running
     - 

 python module subprocess
    - want to use python to run cli commands
    - run bash in python
    - 

python3 add_tags.py <instanceId> <tagKey> <tagValue>
    
"""
instance_id = "i-07c39ce1b58fd42fb"

def add_tags(instance_id, tag_key, tag_value):
    






def main():
    # Checking for number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 add_tags.py <instanceId> <tagKey> <tagValue>")
        sys.exit(1)

    # Now access command line arguments
    instance_id = sys.argv[1]
    tag_key = sys.argv[2]
    tag_value = sys.argv[3]

    # call add_tags function

    add_tags(instance_id, tag_key, tag_value)







main()