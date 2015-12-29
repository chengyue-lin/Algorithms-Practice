string = raw_input()
 
found = False
count = {}
for x in string:
	count[x] = count.get(x, 0) + 1

odd_count = 0
for val in count.values():
	if val % 2 != 0:
		odd_count += 1

found = False if odd_count > 1 else True

if not found:
    print("NO")
else:
    print("YES")