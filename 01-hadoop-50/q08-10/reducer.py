#!/usr/bin/env python

import sys

if __name__ == '__main__':

    curkey = None
    sum = None
    avg = None
    count = 1
    
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)
                
        if sum is None:
            sum = 0
            
        if avg is None:
            avg = 0

        if key == curkey:
            sum = sum + val
            count = count + 1
            avg = sum / count            
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, avg))
            curkey = key
            sum = val
            avg = val
            count = 1
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, sum, avg))
