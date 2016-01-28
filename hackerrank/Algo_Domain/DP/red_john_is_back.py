import math

def get_prime(n):
	is_prime = [False] * 2 + [True] * (n - 1)
	for x in xrange(int(math.ceil(math.sqrt(n)))):
		if is_prime[x]:
			for i in xrange(x*x, n + 1, x):
				is_prime[i] = False
	return [i for i, prime in enumerate(is_prime) if prime]

def patterns(n):
	ways = 1
	v = 0
	while n >= 4:
		v += 1
		n -= 4
		ways += (math.factorial(n + v)/(math.factorial(n) * math.factorial(v)))
	# print "ways", ways
	count = len(get_prime(ways))
	return count

def main():
	t = int(raw_input())
	for __ in xrange(t):
		n = int(raw_input())
		print patterns(n)

if __name__ == "__main__":
	main()