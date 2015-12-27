t = int(raw_input())
for __ in xrange(t):
	n = int(raw_input())
	a = int(raw_input())
	b = int(raw_input())

	end = set()
	j = n - 1
	for i in xrange(0, n):
		val = (a * j) + (b * i)
		end.add(val)
		j-=1
	print " ".join(map(str, sorted(end)))