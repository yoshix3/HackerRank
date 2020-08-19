#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    ma = a[len(a)-1]
    mb = b[0]
    ab = a + b

    result = []
    for i in range(ma, mb+1):
        cnt = 0
        for j in ab:
            if(i>j and i%j==0):
                cnt += 1
            elif(i<=j and j%i==0):
                cnt += 1
        if(cnt==len(ab)):
            result.append(i)
    return len(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
