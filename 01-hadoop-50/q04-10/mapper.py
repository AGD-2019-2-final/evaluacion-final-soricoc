#! /usr/bin/env python

import sys
if __name__ == "__main__":
    for line in sys.stdin:
        cr = line.split()[0]
        sys.stdout.write("{}\t1\n".format(cr))
