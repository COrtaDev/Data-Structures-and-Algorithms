#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # iterate over the arr
    # take the sum of the indices of the diagonal
    # for example, when len(arr) is 3 the following is true:
    # d1 = arr[0][0] + arr[1][1] + arr[2][2]
    # d2 = arr[0][2] + arr[1][1] + arr[2][0]
    # when the len(arr) is 5 the following is true:
    # d1 = arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3]+arr[4][4]
    # d2 = arr[0][4]+arr[1][3]+arr[2][2]+arr[3][1]+arr[4][0]
    # we can define that in terms of i to calculate j without 2 loops
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        d1 += arr[i][i]
        d2 += arr[i][(len(arr) - 1) - i]
        
    diff = abs(d1-d2)
    
    return diff

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
