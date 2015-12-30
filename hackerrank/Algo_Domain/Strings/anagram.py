t = int(raw_input())
for __ in xrange(t):
	s = raw_input()
	if len(s) % 2 == 0:
		s1 = s[:len(s)/2]
		s2 = s[len(s)/2:]

		dict1 = {}
		dict2 = {}

		for x in s1:
			dict1[x] = dict1.get(x, 0) + 1

		for x in s2:
			dict2[x] = dict2.get(x, 0) + 1

		count = 0
		while len(dict1):
			 key, val = dict1.popitem()
			 if dict2.has_key(key):
				val2 = val - dict2.pop(key)
				if val2 > 0:
			 		count += (val2)
			 else:
			 	count += val

		print count
	else:
		print -1