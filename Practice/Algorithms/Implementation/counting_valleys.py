#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    ud = 0
    cnt = 0
    valley = False
    for a in range(n):
        if(s[a:a+1] == 'U'):
            ud += 1
        else:
            ud -= 1
        if(ud<0):
            valley = True
        elif(ud==0):
            if(valley):
                cnt += 1
                valley = False
        else:
            pass
    return(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
