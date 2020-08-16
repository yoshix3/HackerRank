#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    s = ''
    for x in range(n):
        s = s + '#'
        spc = ''
        for y in range(n-x-1):
            spc = spc + ' '
        print(spc + s)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
