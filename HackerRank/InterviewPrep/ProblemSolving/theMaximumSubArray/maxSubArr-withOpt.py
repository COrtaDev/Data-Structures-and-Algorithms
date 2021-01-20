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
    if len(arr) >= 50000:
        # We will have an optimized algo for very large data sets
        # Here we should short circuit as early as possible
        # sum only positive integers of the array
        largeSubArrSum = 0
        largeSum = 0
        for l in range(len(arr)):
            if arr[l] > 0:
                largeSum += arr[l]
        # There is probably a way to optimize the subArr method
        # Perhaps short-circuit when you hit negative value? 
        # Take small slices a until you hit a negative, saving the highest sum along the way
        # This way we are only looking at arrays made of positive values.
        # Also we could be summing all positives along the way so we don't need both loops
        for m in range(len(arr)):
            for o in range(m + 1, len(arr)):
                if arr[m] < 0:
                    break # increment the outer loop immediately
                elif arr[m] > 0 and arr[o] > 0:
                    continue # increment the inner loop
                elif arr[m] > 0 and arr[o] < 0:
                    #only reassign if we found a new biggest sum
                    if largeSubArrSum < sum(arr[m:o]):
                        largeSubArrSum = sum(arr[m:o])
                    m = o+1 # we jump to the end of where you just were
                    break       
                # at this point we have summed all positives and need to jump to a positive once again
        return largeSubArrSum, largeSum
                 
    else:
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
        if arr[0] >= 0: # When the first element is larger than 0, every element is therefore positive
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
