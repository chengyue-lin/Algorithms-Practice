t = int(raw_input())
for __ in xrange(t):
	s = raw_input().strip()
	prev = ""
	count = 0
	for x in s:
		if prev == x:
			count+=1
		prev = x
	print count