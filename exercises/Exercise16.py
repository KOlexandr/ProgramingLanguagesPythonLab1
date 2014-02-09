__author__ = 'KOL'

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime
import struct

maxint = 2 ** (struct.Struct('i').size * 8 - 1) - 1

tlds = ('com', 'edu', 'net', 'org', 'gov')
file = open("redata.txt", "w")
for i in range(randrange(5, 11)):
    # pick date
    dtint = randrange(maxint)
    # date string
    dtstr = ctime(dtint)
    # login is shorter
    llen = randrange(4, 7)
    login = ''.join(choice(lc) for j in range(llen))
    # domain is longer
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))
    file.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))

file.close()
