"""
For n distinct integer x1, x2, . . . xn with positive weights w1, w2, . . . , wn such that sum of all weights is 1,
the weighted median is the element x_k satisfying
Sum of (w_i) for all i such that (x_i < x_k) < 1/2 
and 
Sum of (w_i) for all i such that (x_i > x_k) ≤ 1/2
Show how to compute the weighted median in Θ(n) worst-case using a linear-time selection
algorithm
"""
def linear_weight_selection(x, left, right):
	m = select(x, len(x)//2)
	b, c = [], []
	for x in a:
		if x[0] < m[0]:
			left += x[1]
			b += [x]
		elif x[0] > m[0]:
			right += x[1]
			c += [x]
	if left < 0.5 and right <= 0.5:
		return m
	if left >= 0.5:
		return linear_weight_selection(b, 0, right)
	return linear_weight_selection(c, left, 0)