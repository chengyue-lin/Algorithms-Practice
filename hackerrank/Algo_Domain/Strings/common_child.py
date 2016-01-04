s1 = raw_input().strip()
s2 = raw_input().strip()

x = {}
max_ = 0

for i in xrange(len(s1) + 1):
	for j in xrange(len(s2) + 1):
		if i == 0 or j == 0:
			x[i, j] = 0
		elif s1[i - 1] == s2[j - 1]:
			x[i, j] = x[i - 1, j - 1] + 1
		else:
			x[i, j] = max(x[i - 1, j], x[i, j - 1])
		if max_ < x[i, j]:
			max_ = x[i, j]

print max_