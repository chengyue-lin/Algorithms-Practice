def quicksort(s, start, stop):
	pivot = s[-1]
	l_i = 0
	s_i = 0
	for i in xrange(len(s)):
		if s[i] < pivot:
			s[s_i], s[i] = s[i], s[s_i]
			s_i = i
		elif s[i] >= pivot:
			l_i = i

def main():
	__ = input()
	s = map(int, raw_input().strip().split())
	quicksort(s, 0, len(s))

main()