import math
from itertools import izip_longest
s = raw_input().strip()
l = len(s)
# print "length", l
un_l = math.sqrt(l)
min_ = int(math.floor(un_l))
max_ = int(math.ceil(un_l))
i, j = 0, 0
for x in xrange(min_, max_ + 1):
	for y in xrange(min_, max_ + 1):
		if x * y >= l:
			if i * j > x * y or (i == 0 and j == 0):
				i = x
				j = y
grid = []
start = 0
for x in xrange(i):
	grid.append(s[start: start + j])
	start += (j)
# print "grid", grid

string = ""
for x in xrange(j):
	for y in xrange(i):
		# print "s[", y, "][", x, "]"
		if x < len(grid[y]):
			string += grid[y][x]
	string += " "

print string.strip()