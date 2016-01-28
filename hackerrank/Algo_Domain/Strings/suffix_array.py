# def sort(s, l):
# 	rank = {}
# 	final_rank = {}
# 	i = 0
# 	for x in s:
# 		rank[x] = ord(x[i]) - ord('a')
# 	# while i < l:
# 	# 	for x in s:
# 	# 		if i < len(x):
# 	# 			r =  ord(x[i]) - ord('a')
# 	# 		else:
# 	# 			r = 0
# 	# 		rank[x] = rank.get(x, 0) + r
# 	# 	print "\n\n"
# 	# 	print "*"*100
# 	# 	print "rank at", i
# 	# 	print rank
# 	# 	i += 1
# 	print rank
# 	return s
	
rank = dict()

def compare(l, r):
	l_rank = rank.get(l, [ord(l[0]) - ord('a')])
	r_rank = rank.get(r, [ord(r[0]) - ord['a']])

	if l_rank[0] == r_rank[0]:
		index = l_rank[1]
	else:
		return l_rank[0] < r_rank[0]

def merge(l, r):
	result, i, j = [], 0, 0
	while i < len(l) and j < len(r):
		if compare(l[i], r[j]):
			result.append(l[i])
			i+=1
		else:
			result.append(r[j])
			j+=1

	result += l[i:]
	result += r[j:]
	return result

def sort(s):
	if len(s) < 2:
		return s
	else:
		m = len(s)/2
		l = sort(s[m:])
		r = sort(s[:m])
		return merge(l, r)

def suffix(s):
	return sort([s[i:] for i in xrange(len(s))]), sorted([s[i:] for i in xrange(len(s))])

def main():
	print suffix(raw_input())

if __name__ == "__main__":
	main()