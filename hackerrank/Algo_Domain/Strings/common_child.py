# import time
s1, s2 = raw_input(), raw_input()
# t1 = time.time()
n, m = len(s1), len(s2)

dp_prev = []
dp_current = []

for __ in xrange(n+1):
    dp_current.append(0)
    dp_prev.append(0)

for i in xrange(n + 1):
    for j in xrange(m + 1):
        if i == 0 or j == 0:
            dp_current[j] = 0
        elif s1[i - 1] == s2[j - 1]:
            dp_current[j] = dp_prev[j - 1] + 1
        else:
            dp_current[j] = max(dp_current[j-1], dp_prev[j])

    for j in xrange(n):
        dp_prev[j] = dp_current[j]

print dp_current[-1]
# print time.time() - t1