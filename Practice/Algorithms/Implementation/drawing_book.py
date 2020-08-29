#!/bin/python3

import os
import sys
import math

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    front = 0
    back = 0
    if(n == p):
        back = 0
    elif(n % 2 == 0):
        back =math.ceil((n-p)/2)
    else:
        print((n-p)/2)
        back =int((n-p)/2)

    front = math.ceil((p-1)/2)

    if(front>back):
        return back
    else:
        return front

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
