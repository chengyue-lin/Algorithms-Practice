t = int(raw_input())

s1 = set(raw_input())
for __ in xrange(t - 1):
	s1 = s1.intersection(raw_input())

print len(s1)