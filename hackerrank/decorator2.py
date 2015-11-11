from sys import argv
from operator import itemgetter

def format(func):
	def modifier(information):
		information.sort(key=itemgetter(2))
		return func([('Mr. ' if x[3] == 'M' else 'Ms. ') + x[0] + ' ' + x[1] for x in information])
	return modifier

@format
def print_names(information):
	for info in information:
		print info

def main(input_file):
	cases = None
	with open(input_file, 'r') as f:
		cases = f.readlines()
	cases = [case.split() for case in cases[1:]]
	print_names(cases)


if __name__ == '__main__':
	if len(argv) == 1:
		main('input')
	else:
		main(argv[1])