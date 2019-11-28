#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        k = line.split(',')[1][:1]
        sys.stdout.write("{}\t{}".format(k, line))
