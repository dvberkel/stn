#! /usr/bin/env python

import sys

def s(s0, s1):
    return 6 * s1 - s0

def t(t0, t1):
    return 6 * t1 - t0 + 2

if __name__ == '__main__':
    n = 20
    if (len(sys.argv) == 2):
        n = int(sys.argv[1])
    s0 = 0
    s1 = 1
    t0 = 0
    t1 = 1
    while (n > 0):
        sn = s(s0, s1)
        s0 = s1
        s1 = sn
        tn = t(t0, t1)
        t0 = t1
        t1 = tn
        print "{0},{1}".format(sn, tn)
        n -= 1
