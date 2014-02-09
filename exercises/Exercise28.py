__author__ = 'KOL'

from Tools.Scripts.ftpmirror import raw_input
import re


matcher = re.compile(r"\b(?:\d{3}[-]|)\d{3}[-]\d{4}\b")
while True:
    testText = raw_input("Please, input string: ")
    result = matcher.findall(testText)
    if len(result) != 0:
        print("matched")
        print(result)
    else:
        print("not matched")