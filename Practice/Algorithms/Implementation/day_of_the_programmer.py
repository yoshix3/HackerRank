#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    d = 0
    jan = 31
    mar = 31
    apl = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    if(year<1918):
        if(year % 4 == 0):
            feb = 29
        else:
            feb = 28
    elif(year==1918):
        feb = 15
    else:
        if(year % 400 == 0):
            feb = 29
        elif(year % 4 == 0 and year % 100 != 0 ):
            feb = 29
        else:
            feb = 28
    d = 256 - (jan+feb+mar+apl+may+jun+jul+aug)
    print (d)
    result = "{}.09.{}".format(d, year)
    print (result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
