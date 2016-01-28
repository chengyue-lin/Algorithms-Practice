def max_subarray(arr):
	current_index = 0
	current_sum = 0
	best_sum = 0
	best_start_index = -1
	best_end_index = -1

	for i in xrange(len(arr)):
		val = current_sum + arr[i]
		if val > 0:
			if current_sum == 0:
				current_index = i
			current_sum = val
		else:
			current_sum = 0
		if current_sum > best_sum:
			best_sum = current_sum
			best_start_index = current_index
			best_end_index = i
	result = arr[best_start_index: best_end_index + 1]
	return result if len(result) else [max(arr)]

def main():
	t = int(raw_input())
	for __ in xrange(t):
		_ = int(raw_input())
		arr = map(int, raw_input().split())
		print sum(max_subarray(arr)),
		ar2 = [x for x in arr if x > 0]
		print sum(ar2 if len(ar2) else [max(arr)])

if __name__ == "__main__":
	main()