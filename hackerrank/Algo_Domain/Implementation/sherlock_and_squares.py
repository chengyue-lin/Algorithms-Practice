import math
t = int(raw_input())
for __ in xrange(t):
	x, y = raw_input().split()
	x = int(x)
	y = int(y)
	count = 0
	num = math.ceil(math.sqrt(x))
	num2 = 0
	while num2 <= y:
		num2 = num ** 2
		if num2 >= x and num2 <= y:
			count += 1
		num += 1
	print count