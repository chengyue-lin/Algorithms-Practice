def minimal_string(s1, s2):
	answer = ""
	while s1 and s2:
		answer += s1.pop(0) if ord(s1[0]) < ord(s2[0]) else s2.pop(0)
	while s1:
		answer += s1.pop(0)
	while s2:
		answer += s2.pop(0)
	return answer

def main():
	t = int(raw_input())
	for __ in xrange(t):
		s1, s2 = list(raw_input().strip()), list(raw_input().strip())
		print minimal_string(s1, s2)
main()