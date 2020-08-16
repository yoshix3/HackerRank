#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h = s[0:2]
    ap = s[8:10]
    if("PM"==ap):
        if(int(h)<12):
            h = int(h)+12
    else:
        if(h == '12'):
            h = '00'
    return "{}{}".format(h, s[2:8])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
