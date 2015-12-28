def rotate(matrix, x, y):
	min_x, max_x = -1, x
	min_y, max_y = -1, y
	while max_x - min_x > 1 and max_y - min_y > 1:
		# print "*"*100
		min_x += 1
		min_y += 1
		max_x -= 1
		max_y -= 1
		# print "x = [",min_x,",",max_x,"]", "y = [",min_y,",",max_y,"]"
		temp1 = matrix[min_x][min_y]
		temp2 = matrix[max_x][max_y]
		for i in xrange(min_y, max_y):
			matrix[min_x][i] = matrix[min_x][i + 1]
			# print "[", min_x,"][",i,"] <- [",min_x,"][",i + 1,"]"

		# print ""			

		for i in xrange(max_y - 1, min_y - 1, -1):
			matrix[max_x][i + 1] = matrix[max_x][i]
			# print "[", max_x,"][",i + 1,"] <- [",max_x,"][",i,"]"

		# print "\n"

		for j in xrange(max_x - 1, min_x - 1, -1):
			matrix[j + 1][min_y] = matrix[j][min_y]
			# print "[", j+1,"][", min_y,"] <- [", j,"][", min_y,"]"
			
		# print ""

		for j in xrange(min_x, max_x - 1):
			matrix[j][max_y] = matrix[j + 1][max_y]
			# print "[", j,"][", max_y,"] <- [", j + 1,"][", max_y,"]"

		# print "\n"

		# print "[", min_x + 1,"][", min_y,"] <- [", min_x,"][", min_y,"]"
		# print "[", max_x - 1,"][", max_y,"] <- [", max_x,"][", max_y,"]"

		matrix[min_x + 1][min_y] = temp1
		matrix[max_x - 1][max_y] = temp2
	return matrix

m, n, r = map(int, raw_input().strip().split())
mat = []
for __ in xrange(m):
	mat.append(map(int, raw_input().strip().split()))
# print mat
for __ in xrange(r):
	rotate(mat, m, n)

for x in xrange(m):
	for y in xrange(n):
		print mat[x][y],
	print ""