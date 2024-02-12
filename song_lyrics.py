#!/usr/bin/python3
import re

pattern = r'^\[Verse\d+\].*$'

song = input("Enter song lyrics in the format '[Verse X] some lyrics': ")

match = re.match(pattern, song)

if match:
    print("match")
else:
    print("not match")