#!/usr/bin/env python

import sys

if __name__ == '__main__':

    curkey = None
    mx = None
    mn = None
    
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
        
        if mx is None:
            mx = val
            
        if mn is None:
            mn = val

        if key == curkey:
            mx = max(val, mx)
            mn = min(val, mn)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, mx, mn))
            curkey = key
            mx = val
            mn = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, mx, mn))
