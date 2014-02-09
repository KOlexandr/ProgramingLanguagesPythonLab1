__author__ = 'KOL'

from Tools.Scripts.ftpmirror import raw_input
import re

#first and last names must begin with capital letter and must consist only letters
#initial must be capital letter
matcher = re.compile(r"\b[A-Z][a-zA-Z]*\b[ ]\b[A-Z]\b")
while True:
    testText = raw_input("Please, input string: ")
    result = matcher.findall(testText)
    if len(result) != 0:
        print("matched")
        print(result)
    else:
        print("not matched")