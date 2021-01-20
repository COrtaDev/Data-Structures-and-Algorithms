#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesThatHit = 0
    orangesThatHit = 0
    for i in range(len(apples)):
        d = a + apples[i]
        if d >= s and d <= t:
            applesThatHit += 1
    for j in range(len(oranges)):
        d = b + oranges[j]
        if d >= s and d <= t:
            orangesThatHit += 1
    print(applesThatHit)
    print(orangesThatHit)
    return 

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
