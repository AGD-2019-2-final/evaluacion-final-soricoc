#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        a = line.split()[0]
        b = line.split()[1]
        c = line.split()[2]
        sys.stdout.write("{};{}\t{}\t{}\n".format(c, a, b, c))
