t = int(raw_input())
for __ in xrange(t):
	s1, s2 = raw_input(), raw_input()
	dict1 = {}
	answer = "NO"
	for x in s1:
		dict1[x] = 1
	for x in s2:
		if dict1.has_key(x):
			answer = "YES"
			break
	print answer