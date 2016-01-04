t = int(raw_input())
for __ in xrange(t):
	s = raw_input()
	count = 0
	for x, y in zip(s[:len(s)/2+1], s[len(s):len(s)/2-1:-1]):
		count+= abs(ord(x) - ord(y))
	print count