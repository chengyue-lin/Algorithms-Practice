#!/bin/python

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    max_sum = -sys.maxint
    arr = [0] * n
    for a, b, k in queries:
        arr[a - 1] += k
        if((b)<len(arr)): arr[b] -= k
        print arr
    max = x = 0
    for i in arr:
        x = x+i;
        if(max_sum < x): max_sum = x;
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

