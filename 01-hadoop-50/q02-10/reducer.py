#!/usr/bin/env python

import sys

if __name__ == '__main__':

    curkey = None
    max_amnt = None
    
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        
        if max_amnt is None:
            max_amnt = val

        if key == curkey:
            max_amnt = max(val, max_amnt)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, max_amnt))
            curkey = key
            max_amnt = val
    sys.stdout.write("{}\t{}\n".format(curkey, max_amnt))
