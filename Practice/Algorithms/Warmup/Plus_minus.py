#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for x in arr:
        if(x>0):
            p += 1
        elif(x<0):
            n += 1
        else:
            z += 1
    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
