t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    n2 = n
    count = 0
    while n2 > 0:
    	x = n2 % 10
    	if x != 0:
	    	if n % x == 0:
	    		count += 1
    	n2 /= 10
    print count