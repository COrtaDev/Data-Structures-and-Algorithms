#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    # each iteration we will need to print n chars
    # so if n = 6, first loops will print 5 spaces and 1 #
    # the following loop will print 4 spaces and 2 #
    for i in range(1, n+1):
        # starting at 1 allows us to get the number of hashMarks
        # the number of whitespace is n - i
        print(" "*(n-i)+"#"*i)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
