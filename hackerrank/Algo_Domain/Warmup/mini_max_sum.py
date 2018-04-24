#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    arr = sorted(arr)
    print(sum(arr[:4]), sum(arr[-4:]))

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
