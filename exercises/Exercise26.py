__author__ = 'KOL'

import re

file = open("redata.txt", "r")
lines = file.readlines()
file.close()

matcher = re.compile(r"[a-z]+@[a-z]+\.(?:com|edu|net|org|gov)")
for i in lines:
    print(matcher.sub("kolexandr.13@gmail.com", i))