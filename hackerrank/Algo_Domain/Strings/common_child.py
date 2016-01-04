s1 = raw_input().strip()
s2 = raw_input().strip()

x = [[0 for __ in xrange(len(s2) + 1)] for __ in xrange(len(s1) + 1)]
max_ = 0

for i in xrange(len(s1)):
    for j in xrange(len(s2)):
        if s1[i] == s2[j]:
            x[i + 1][j + 1] = x[i][j] + 1
        else:
            x[i + 1][j + 1] = max(x[i][j + 1], x[i + 1][j])
        if max_ < x[i + 1][j + 1]:
            max_ = x[i + 1][j + 1]

print max_