#!/usr/bin/python3
"""import regular expressions"""
import re
string = """Date: Today is 15-Feb-2000
            IP addresses: 192.168.000.111
         """
pattern = r"\d{2}-[A-Za-z]{3}-\d{4}"
matches = re.search(pattern, string)
if matches:
    Date = matches[0]
    print("Date:", matches)
else:
    print("no matches.")