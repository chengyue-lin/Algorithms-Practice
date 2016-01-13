def do_stuff(s, n):
	elem = []
	print s, n
	return
	while len(s) or s[0] != ')':
		a = s.pop(0)
		if a != '(':
			return

def main():
	t = int(raw_input())
	for __ in xrange(t):
		s, n = raw_input().split()
		do_stuff(list(s), n)

main()