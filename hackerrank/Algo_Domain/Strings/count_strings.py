def do_stuff(s, n):
	elem = []
	while len(s):
		a = s.pop(0)
		
			

def main():
	t = int(raw_input())
	for __ in xrange(t):
		s, n = raw_input().split()
		do_stuff(list(s), n)

main()