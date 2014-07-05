#! /usr/bin/env python

def s(s0, s1):
    return 6 * s1 - s0

def t(t0, t1):
    return 6 * t1 - t0 + 2

if __name__ == '__main__':
    print "{0},{1}".format(s(0, 1), t(0,1))
