n = int(raw_input().strip())
for x in xrange(n - 1, -1, -1):
	if x != 0:
		print " " * (x - 1),
	print "#" * (n - x)