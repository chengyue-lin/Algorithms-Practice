t = int(raw_input())
for __ in xrange(t):
	string = raw_input()
	length = len(string)
	answer = "Funny"
	for i, j in zip(xrange(0, length - 1), xrange(length - 1, 0, -1)):
		if abs(ord(string[i]) - ord(string[i + 1])) != abs(ord(string[j]) - ord(string[j - 1])):
			answer = "Not Funny"
	print answer