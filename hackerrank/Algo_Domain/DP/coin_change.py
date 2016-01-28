def count(arr, m, n):

	table = [[0 for __ in xrange(m)] for _ in xrange(n + 1)]

	for i in xrange(m):
		table[0][i] = 1

	for i in xrange(1, n+1):
		for j in xrange(m):
			x = table[i - arr[j]][j] if i - arr[j] >= 0 else 0

			y = table[i][j - 1] if j > 0 else 0

			table[i][j] = x + y

	return table[-1][-1]

def main():
	n, m = map(int, raw_input().split())
	arr = map(int, raw_input().split())
	print count(arr, m, n)
 
if __name__ == "__main__":
	main()