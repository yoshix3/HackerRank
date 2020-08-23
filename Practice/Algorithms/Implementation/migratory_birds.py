#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    type_list = [0, 0, 0, 0, 0, 0]
    for i in arr:
        type_list[i] += 1
    # print(type_list)

    max_type = 0
    max_cnt = 0
    for i, t in enumerate(type_list):
        if(max_cnt < t):
            max_type = i
            max_cnt = t
    # print(max_type)
    return max_type

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
