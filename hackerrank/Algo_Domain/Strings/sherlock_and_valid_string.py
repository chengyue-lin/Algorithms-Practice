from collections import Counter

def is_valid(s):
	c = Counter(s).values()
	c.sort()
	x = Counter(c).values()
	if len(x) == 1:
		return True
	x.sort()
	if x[0] == 1 and len(x) == 2:
		return True
	return False

def main():
	print "YES" if is_valid(raw_input()) else "NO"

main()