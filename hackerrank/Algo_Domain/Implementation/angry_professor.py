t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    threshold = 0
    for std_time in a:
    	if std_time <= 0:
    		threshold += 1
    if threshold < k:
    	print "YES"
    else:
    	print "NO"