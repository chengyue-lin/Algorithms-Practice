from collections import Counter
t = int(raw_input())
for __ in xrange(t):
	s = raw_input()
	l = len(s)

	count = 0
	m = l
	for i in xrange(1, l):
		subs = []
		for j in xrange(m):
			subs.append(s[j:i+j])
		m -= 1

		for x in xrange(len(subs)):
			for y in xrange(x + 1, len(subs)):
				one = Counter(subs[x])
				two = Counter(subs[y])
				if len((one - two)) == 0:
					count += 1
	print count
