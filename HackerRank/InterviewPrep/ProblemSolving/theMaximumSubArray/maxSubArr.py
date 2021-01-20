#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubarray function below.
def maxSubarray(arr):
    # the subarray will be a slice of the array where all elements are contiguous
    # the subsequence however are elements that are non contiguous
    # we observe that if all elements are negative the max subseqence therefore is the 
    #   largest negative number aka: the number closest to 0.
    # we observe that if all the numbers are positive, the max sum will be the sum of all
    #   elements in that array.
    # we observe that the maximum subsequence can be found by removing all negative numbers for the
    #   array and summing them together
    # the most time-complex behavior will be associated with finding the subarray sum of all subarrays
    #   in a given array and returning the max sum of that subarray
    # Currently we time out for certain test cases, they must be extremely long arrays
    # We will look for optimizations first
    # if(len(arr) >= 50000):
    #     print(len(arr))
    #     return 
    print(len(arr))
    
    
    # The following code is adequate for all but 1 test case:
    maxSubArrSum = sum(arr)
    # This handles finding the max subArr sum:
    for i in range(len(arr)):
        for j in range(len(arr), i, -1):
            currentSum = sum(arr[i:j])
            if maxSubArrSum < currentSum:
                maxSubArrSum = currentSum
    arr.sort()
    # We can peek at the first and last elements of the sorted array
    # If they are both positive we can return the sum of the entire array
    if arr[0] > 0: # When the first element is larger than 0, every element is therefore positive
        return maxSubArrSum, sum(arr)
    if arr[-1] < 0: # When the last element is negative, it will be the largest int in the array
        return maxSubArrSum, arr[-1]
    # At this point we have an array of negative and positive numbers
    # We will iterate through the array and find the first postive value
    for k in range(1, len(arr)): 
        if arr[k] > 0:
            return maxSubArrSum, sum(arr[k:len(arr)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
