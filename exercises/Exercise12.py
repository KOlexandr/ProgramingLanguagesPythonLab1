__author__ = 'KOL'

from Tools.Scripts.ftpmirror import raw_input
import re


matcher = re.compile(r"w{3}\.[a-zA-Z0-9_-]+\.(?:[a-zA-Z]*|(?:[a-zA-Z]+\.[a-zA-Z]+)+)$")
while True:
    testText = raw_input("Please, input string: ")
    result = matcher.findall(testText)
    if len(result) != 0:
        print("matched")
        print(result)
    else:
        print("not matched")