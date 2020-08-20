#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = 0
    max = 0
    min_cnt = 0
    max_cnt = 0
    for i, score in enumerate(scores):
        if(i == 0):
            min = score
            max = score
        else:
            if(min>score):
                min_cnt += 1
                min = score
            elif(max<score):
                max_cnt += 1
                max = score

    result = [max_cnt, min_cnt]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
