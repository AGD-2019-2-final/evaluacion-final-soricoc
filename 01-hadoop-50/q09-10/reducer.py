#!/usr/bin/env python

import sys
from operator import itemgetter

if __name__ == '__main__':  
    lines = sys.stdin.readlines()
    sortedlist = sorted(lines, key=lambda x:int(x.split(";")[0]))
    for i in range(6):
         print(sortedlist[i].split(';')[-1]),
