import math

def isprime(n):
    """Returns True if n is prime"""
    if n == 1:
    	return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def patterns(n):
	ways = 1
	v = 0
	while n >= 4:
		v += 1
		n -= 4
		ways += (math.factorial(n + v)/(math.factorial(n) * math.factorial(v)))
	# print "ways", ways
	count = 0
	for x in xrange(ways + 1):
		if isprime(x):
			count += 1
	return count

def main():
	t = int(raw_input())
	for __ in xrange(t):
		n = int(raw_input())
		print patterns(n)

if __name__ == "__main__":
	main()