#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    x = max(ar)
    return ar.count(x)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()

