t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    x = n
    i = 0
    answer = "-1"
    while x >= 0:
    	x = (n - (5 * i))
    	i+=1
    	if x % 3 == 0 and x >= 0:
    		answer = "5"*x + (n - x) * "3"
    		x = -1
    print answer