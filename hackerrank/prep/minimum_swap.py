#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    _sum = 0
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            j = arr[i]-1
            print i, j
            arr[i] = arr[i] + arr[j]
            arr[j] = arr[i] - arr[j]
            arr[i] = arr[i] - arr[j]
            _sum += 1
            i -= 1
        i+=1
    return _sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
