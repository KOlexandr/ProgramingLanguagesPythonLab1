__author__ = 'KOL'

from Tools.Scripts.ftpmirror import raw_input
import re


matcher = re.compile(r"\b[bh][aiu]t\b")
while True:
    testText = raw_input("Please, input one word: ")
    result = matcher.findall(testText)
    if len(result) != 0:
        print("matched")
        print(result)
    else:
        print("not matched")