__author__ = 'KOL'

import re

file = open("redata.txt", "r")
lines = file.readlines()
file.close()

matcher = re.compile(r"[a-z]+@[a-z]+\.(?:com|edu|net|org|gov)")
for i in lines:
    email = matcher.findall(i)[0]
    login = str(email.split("@")[0])
    domains = str(email.split("@")[1])
    print("login=" + login + ",\tdomains=" + domains)