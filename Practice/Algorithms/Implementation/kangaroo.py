#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    result = ""
    if(x1<x2 and v1<v2):
        result="NO"
    elif(x1>x2 and v1>v2):
        result="NO"
    else:
        for i in range(10000):
            a = x1 + v1*i
            b = x2 + v2*i
            if(a==b):
                result="YES"
                break
        else:
            result="NO"
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
