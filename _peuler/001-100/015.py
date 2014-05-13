n = 21
grid = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(0)
    grid.append(temp)
    
grid[0][0] = 1

for i in range(n):
    for j in range(n):
        if i - 1>=0:
            grid[i][j] = grid[i][j] + grid[i - 1][j]
        if j - 1>=0:
            grid[i][j] = grid[i][j] + grid[i][j - 1]

print grid[n - 1][n - 1]
