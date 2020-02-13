#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        l = line.split()[0]
        c = line.split()[2]
        sys.stdout.write("{}\t{}\n".format(l, c))
