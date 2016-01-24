def flip_bits(i):
	mask = (2 ** 32) - 1
	return ~i & mask

if __name__ == "__main__":
	t = input()
	for __ in xrange(t):
		print flip_bits(int(raw_input()))