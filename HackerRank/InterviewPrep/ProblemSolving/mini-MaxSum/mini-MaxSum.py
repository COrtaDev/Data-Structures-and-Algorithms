#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # we should first sort the array to ensure that it is ordered from lowest to highest int values
    # if this is the case, the min will be the first 4 elements
    # and the max will be the last 5 elements.
    arr.sort()
    min = arr[0]+arr[1]+arr[2]+arr[3]
    max = arr[1]+arr[2]+arr[3]+arr[4]
    print(min,max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
