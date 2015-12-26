n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

zero = 0
pos = 0
neg = 0

for x in arr:
	if x == 0:
		zero += 1
	elif x > 0:
		pos += 1
	else:
		neg += 1

print pos/float(n)
print neg/float(n)
print zero/float(n)