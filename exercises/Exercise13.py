__author__ = 'KOL'

from Tools.Scripts.ftpmirror import raw_input
import re


def get_type(string):
    matcher = re.compile(r"<type '[a-z_]+'>")
    if matcher.match(string):
        matcher = re.compile(r"'[a-z_]+'")
        return matcher.findall(string)
    else:
        return None

while True:
    testText = raw_input("Please, input string: ")
    print(get_type(testText))


