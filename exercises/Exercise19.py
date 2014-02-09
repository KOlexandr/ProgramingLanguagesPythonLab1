__author__ = 'KOL'

import re

file = open("redata.txt", "r")
lines = file.readlines()
file.close()

matcher = re.compile(r"^[A-Z][a-z]{2}[ ][A-Z][a-z]{2}[ ]{1,2}[\d]{1,2}[ ]\d{2}:\d{2}:\d{2}[ ]\d{4}")
for i in lines:
    print(matcher.findall(i)[0])