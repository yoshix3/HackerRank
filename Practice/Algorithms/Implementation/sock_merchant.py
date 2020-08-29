#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dic = {}
    for a in ar:
        if(a in dic):
            dic[a] += 1
        else:
            dic[a] = 1

    cnt = 0
    for i in dic:
        print(dic[i] / 2)
        if(dic[i] / 2 > 0):
            cnt += int(dic[i]/2)

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
