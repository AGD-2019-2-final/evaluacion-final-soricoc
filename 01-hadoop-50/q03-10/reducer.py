#!/usr/bin/env python

import sys

if __name__ == '__main__':   
    for line in sys.stdin:
        val = line.split('\t')[-1]
        sys.stdout.write("{}".format(val))
