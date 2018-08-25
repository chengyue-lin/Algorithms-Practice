#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribe = dict()
    _sum = 0
    for i in xrange(len(q)):
        j = 0
        while (i + 1 != q[j]):
            j += 1
        while j != i:
            q[j] = q[j] + q[j-1]
            q[j - 1] = q[j] - q[j-1]
            q[j] = q[j] - q[j-1]
            bribe[q[j]] = bribe.get(q[j], 0) + 1
            if bribe.get(q[j], 0) > 2:
                print "Too chaotic"
                return
            _sum += 1
            j -= 1
    print _sum

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

# better solution:



import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    _sum = 0
    for i in reversed(xrange(len(q))):
        if q[i] - (i + 1) > 2:
            print "Too chaotic"
            return
        for j in  xrange(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                _sum += 1
    print _sum

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

