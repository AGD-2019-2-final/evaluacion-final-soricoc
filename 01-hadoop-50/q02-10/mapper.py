#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        pp = line.split(',')[3]
        am = line.split(',')[4]
        sys.stdout.write("{}\t{}\n".format(pp, am))
