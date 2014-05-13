def dfs(grid, r, c, m, R, C, M):

    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j] != "*":
                #re-evaluate numbers
                grid[i][j] = 0
                for x in xrange(-1, 2):
                    for y in xrange(-1, 2):
                        if i + x >= 0 and i + x < R and j + y >= 0 and j + y < C:
                            if grid[i + x][j + y] == "*":
                                grid[i][j] += 1
                grid[i][j] = str(grid[i][j])

    if m > M:
        #dfs
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                copyGrid = []
                for x in xrange(R):
                    copyRow = []
                    for y in xrange(C):
                        copyRow.append(grid[x][y])
                    copyGrid.append(copyRow[:])
                # if this location is a mine, try to take it out and see if we get one click
                if r + i >= 0 and r + i < R and c + j >= 0 and c + j < C and grid[r + i][c + j] == "*":
                    copyGrid[r + i][c + j] = "."
                    dfs(copyGrid, r + i, c + j, m - 1, R, C, M)
    else:
        #we have enough mines, evaluate one-click win
        return True





def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T-2):
        R, C, M = map(int, fin.readline().strip().split(' '))
        answer = ""
        print R, C, M
        grid = []
        for i in xrange(R):
            row = []
            for j in xrange(C):
                row.append("*")
            grid.append(row[:])
        grid[0][0] = "."
        print grid
        answer = dfs(grid, 0, 0, R*C-1, R, C, M)
        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("C-tiny")
