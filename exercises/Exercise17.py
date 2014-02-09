__author__ = 'KOL'

from numpy.core.multiarray import zeros
import re


daysChoose = zeros(7, dtype=int)

file = open("redata.txt", "r")
lines = file.readlines()
file.close()

matcher = re.compile(r"[MTWSF][a-z]{2}")

for i in lines:
    day = matcher.findall(i)[0]
    if day == "Mon":
        daysChoose[0] += 1
    elif day == "Thu":
        daysChoose[1] += 1
    elif day == "Wed":
        daysChoose[2] += 1
    elif day == "Tue":
        daysChoose[3] += 1
    elif day == "Fri":
        daysChoose[4] += 1
    elif day == "Sat":
        daysChoose[5] += 1
    elif day == "Sun":
        daysChoose[6] += 1
print(daysChoose)