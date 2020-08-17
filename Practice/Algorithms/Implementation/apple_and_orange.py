#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_cnt = 0
    orange_cnt = 0
    for apple in apples:
        # print("{} {} {}".format(apple + a, s, t))
        if(s <= apple + a and apple + a <= t):
            apple_cnt += 1
    for orange in oranges:
        # print("{} {} {}".format(orange + b, s, t))
        if(s <= orange + b and orange + b <= t):
            orange_cnt += 1
    print(apple_cnt)
    print(orange_cnt)

if __name__ == '__main__':
    # st = input().split()

    # s = int(st[0])

    # t = int(st[1])

    # ab = input().split()

    # a = int(ab[0])

    # b = int(ab[1])

    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))
    s=7
    t=11
    a=5
    b=15
    m=3
    n=2
    apples=[-2, 2, 1]
    oranges=[5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
