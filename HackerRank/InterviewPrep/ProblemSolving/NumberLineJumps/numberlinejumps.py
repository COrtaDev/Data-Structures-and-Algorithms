#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # We will need to keep track of the number of jumps
    # increment each iteration.
    # calculate the distance each roo is jumping each iteration,
    # if they converge print YES else print NO
    k1 = x1 # these are the initial positions of each roo
    k2 = x2
    jumps = 0
    # print(k1,k2)
    # depending on where they start and their rate of change we can determine if they
    # will ever even have a chance at converging.
    if (k1 > k2 and v1 > v2) or (k1 < k2 and v1 < v2):
        # print("here")
        # return print('NO')
        return "NO"
    if (k1 > k2):
        while k1 > k2:
            jumps += 1
            k1 = (v1*(jumps)) + x1
            k2 = (v2*(jumps)) + x2
            # print(k1,k2)
            if k1 == k2:
                # return print('YES')
                return "YES"
        # return print('NO')
        return "NO"
    else:
        while k1 < k2:
            jumps += 1
            k1 = (v1*(jumps)) + x1
            k2 = (v2*(jumps)) + x2
            # print(k1,k2)
            if k1 == k2:
                # return print('YES')
                return "YES"
        # return print('NO')
        return "NO"
    
        
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
