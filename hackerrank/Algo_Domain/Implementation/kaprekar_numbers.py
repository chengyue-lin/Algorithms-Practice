start = int(raw_input())
end = int(raw_input())
flag = False
for x in xrange(start, end+1):
	sq = x ** 2
	r = sq % (10 ** ((len(str(sq)) + 1)/2))
	l = sq / (10 ** ((len(str(sq)) + 1)/2))
	if x == (r + l):
		print x,
		flag = True
if not flag:
	print "INVALID RANGE"