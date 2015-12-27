t = int(raw_input().strip())
for __ in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    sum = 0
    if (z+y) < x or (z+x) < y:
    	if x < y:
    		sum = (x * b) + ((z + x) * w)
    	else:
    		sum = (y * w) + ((z + y) * b)
    else:
    	sum = (x * b) + (y * w)
    print sum