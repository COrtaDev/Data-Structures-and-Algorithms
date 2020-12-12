#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(q) - 1):
            if q[i] > i + 3:
                print("Too chaotic")
                return
            else:
                if q[i] > q[i + 1]:
                    swap(q, i, i + 1)
                    bribes += 1
                    swapped = True
    print(bribes)
    return
            
def swap(q, idx1, idx2):
    temp = q[idx1]
    q[idx1] = q[idx2]
    q[idx2] = temp

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
