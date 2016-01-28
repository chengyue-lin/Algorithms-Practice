def get_next(s):
	s1 = sorted(s)
	min_ = (-1, ord('a'))
	
	i = 0
	while min_[1] >= ord(s[i]) and i < len(s):
		min_ = i, ord(s[i])
		i += 1

	next_min_ = min_

	while i < len(s):
		if next_min_[1] < ord(s[i]) and ord(s[i]) > min_[1]:
			next_min_ = i, s[i]
		i += 1

	x = list(s)
	x[next_min_[0]], x[min_[0]] = x[min_[0]], x[next_min_[0]]
	x = "".join(x)

	if x == s:
		print "no answer"
	else:
		print x


if __name__ == "__main__":
	t = int(raw_input())
	for __ in xrange(t):
		get_next(raw_input())