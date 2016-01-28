def calculate_dist(rating):
	result = [1 for __ in xrange(len(rating))]

	for i in xrange(1, len(rating)):
		if rating[i] > rating[i - 1]:
			result[i] = result[i - 1] + 1

	for i in xrange(len(rating) - 2, -1, -1):
		if rating[i] > rating[i + 1]:
			if result[i] <= result[i + 1]:
				result[i] = result[i + 1] + 1
	return sum(result)

def main():
	t = int(raw_input())
	rating = []
	for __ in xrange(t):
		rating.append(int(raw_input()))
	print calculate_dist(rating)

if __name__ == "__main__":
	main()