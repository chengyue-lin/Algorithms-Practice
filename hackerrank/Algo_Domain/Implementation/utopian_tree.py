t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    height = 1
    for cycle in xrange(1, n + 1):
    	if cycle % 2 == 0:
    		height += 1
    	else:
    		height *= 2
    print height