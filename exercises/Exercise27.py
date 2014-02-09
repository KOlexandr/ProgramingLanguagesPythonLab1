__author__ = 'KOL'

import re

file = open("redata.txt", "r")
lines = file.readlines()
file.close()

matcher = re.compile(r"\b[A-Z][a-z]{2}\b|\b\d{4}\b")
for i in lines:
    result = matcher.findall(i)
    print(result[1] + ", " + result[0] + ", " + result[2])