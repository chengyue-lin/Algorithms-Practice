s1, s2 = raw_input(), raw_input()

dict1 = {}
dict2 = {}

for x in s1:
	dict1[x] = dict1.get(x, 0) + 1

for x in s2:
	dict2[x] = dict2.get(x, 0) + 1

count = 0

while len(dict1):
	 key, val = dict1.popitem()
	 if dict2.has_key(key):
	 	count += abs(val - dict2.pop(key))
	 else:
	 	count += val

count += sum(dict2.values())

print count