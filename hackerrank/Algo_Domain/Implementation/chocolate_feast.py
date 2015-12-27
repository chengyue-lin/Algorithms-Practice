t = int(raw_input())
for __ in xrange(t):
	n, c, m = map(int, raw_input().strip().split())
	wrapper = num = n/c
	while wrapper >= m:
		remaining = (wrapper % m)
		wrapper = (wrapper/m)
		num += wrapper
		wrapper += remaining
	print num