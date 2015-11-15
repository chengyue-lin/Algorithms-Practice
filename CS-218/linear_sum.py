import sys

def linear_sum(left, right):
    s = 0
    left_sum = -sys.maxint
    left_index = 0
    for i in reversed(xrange(len(left))):
        s += left[i]
        if s > left_sum:
          left_sum = s
          left_index = len(left) - i

    s = 0
    right_sum = -sys.maxint
    right_index = 0
    for i in xrange(len(right)):
        s += right[i]
        if s > right_sum:
          right_sum = s
          right_index = i
    return left_sum + right_sum, left_index, right_index


def max_sub(ar):
    if len(ar) <= 1:
        return ar[0], 0, 0
    m = len(ar)//2
    x, _, _ = max_sub(ar[:m])
    y, _, _ = max_sub(ar[m:])
    z, l, r = linear_sum(ar[:m], ar[m:])
    return max(x, y, z), m - l, m + r

def get_indices(ar):
    val = max_sub(ar)
    return val
    # if val[0] < 0:
    #     return 0, 0
    # else:
    #     return val[1] + 1, val[2] + 1

if __name__ == "__main__":
    # ar = [-2, 11, -4, 13, -5, 2]
    # ar = [1, -3, 4, -2, -1, 6]
    # ar = [-1, 4, -3, 5, -2, -1, 2, 6, -21]
    ar = [1, 6, -5, -6, -4, -9, -10]
    # ar = [-4, -3]
    print get_indices(ar)