#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = None
    for i in xrange(1, 5):
        for j in xrange(1, 5):
            _sum = arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i][j]
            _sum += arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            if (maxSum is None) or (maxSum < _sum):
                maxSum = _sum
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
