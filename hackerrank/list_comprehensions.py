from sys import argv

def main(input_file):
	with open(input_file, 'r') as f:
		cases = f.readlines()
		print [[x, y, z] for x in xrange(int(cases[0]) + 1) for y in xrange(int(cases[1]) + 1) for z in xrange(int(cases[2]) + 1) if x + y + z != int(cases[3])]


if __name__ == '__main__':
	if len(argv) == 2:
		main(argv[1])
	else:
		main('input')