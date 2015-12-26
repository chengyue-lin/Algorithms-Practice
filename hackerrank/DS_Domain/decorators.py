from sys import argv

def format(func):
	def modifier(numbers):
		return func(['+91 ' + x.replace("\n","")[-10:-5] + ' ' + x.replace("\n","")[-5:] for x in numbers])
	return modifier

@format
def format_numbers(numbers):
	for number in sorted(numbers):
		print number

def main(input_file):
	with open(input_file, 'r') as f:
		cases = f.readlines()
		format_numbers(cases[1:])


if __name__ == '__main__':
	if len(argv) == 2:
		main(argv[1])
	else:
		main('input')