t = int(raw_input())

for __ in xrange(t):
	s = list(raw_input().strip())
	i, j, l = 0, len(s) - 1, len(s)
	position = -1
	while i < l/2 and j > l/2:
		if s[i] == s[j]:
			i+=1
			j-=1
		elif s[i] == s[j-1]:
			position = j
			j-=2
			i+=1
		elif s[i+1] == s[j]:
			position = i
			i+=2
			j-=1
		elif position != -1:
			if position < len(s)/2:
				j = j + (i - position) - 1
				i = position
				position = j
				j -= 1
			else:
				i = i - (position - j) + 1
				j = position
				position = i
				i += 1
	print position
