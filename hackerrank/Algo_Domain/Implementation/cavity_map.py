n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
   grid_t = list(raw_input().strip())
   grid.append(grid_t)
for x in xrange(1, n - 1):
    for y in xrange(1, n - 1):
        if grid[x][y] > grid[x - 1][y] and grid[x][y] > grid[x][y - 1] and grid[x][y] > grid[x + 1][y] and grid[x][y] > grid[x][y + 1]:
            grid[x][y] = "X"
for item in grid:
    print "".join(item)