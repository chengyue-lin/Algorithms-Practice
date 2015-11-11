n = input()
info_dict = {}
for __ in xrange(n):
	data = raw_input().split()
	info_dict[data[0]] = sum([float(x) for x in data[1:]])/3

print ("%.2f" % info_dict[raw_input()])