n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)
res = 0
count = 0
for i in xrange(n):
	for j in xrange(i + 1, n):
		new_res = bin(int(topic[i], 2) | int(topic[j], 2)).count("1")
		if new_res > res:
			res = new_res
			count = 1
		elif res == new_res:
			count += 1
print res
print countamp