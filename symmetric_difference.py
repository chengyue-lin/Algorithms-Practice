from sys import argv

def main(input_file):
	with open(input_file, 'r') as f:
		cases = f.readlines()
		set1 = set(map(int, cases[1].split()))
		set2 = set(map(int, cases[3].split()))
		print set1, set2
		for val in set1.union(set2).difference(set1.intersection(set2))):
			print val


if __name__ == '__main__':
	if len(argv) == 2:
		main(argv[1])
	else:
		main('input')