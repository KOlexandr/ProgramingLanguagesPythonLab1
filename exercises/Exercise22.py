__author__ = 'KOL'

import re

file = open("redata.txt", "r")
lines = file.readlines()
file.close()

matcher = re.compile(r"\d{4}")
for i in lines:
    print(matcher.findall(i)[0])