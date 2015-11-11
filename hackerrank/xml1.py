import xml.etree.ElementTree as etree
from sys import argv

def main(input_file):
	with open(input_file, 'r') as f:
		cases = f.readlines()
	xml = ''	
	for line in cases[1:]:
		xml += line	
	tree = etree.ElementTree(etree.fromstring(xml))
	score = 0
	for child in tree.iter():
		score += len(child.items())
	print score

if __name__ == '__main__':
	if len(argv) == 2:
		main(argv[1])
	else:
		main('input')