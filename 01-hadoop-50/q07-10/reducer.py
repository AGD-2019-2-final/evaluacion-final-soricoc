#!/usr/bin/env python

import sys

if __name__ == '__main__':   
    lines = sys.stdin.readlines()
    lines.sort(key=lambda x:int(x.split()[-1]))
    lines.sort(key=lambda x:(x.split()[0]))  
    for line in lines:
         print(line),
