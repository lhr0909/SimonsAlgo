#http://www.angusj.com/sudoku/hints.php

fin = open('096.txt', 'r')

def printGrid(grid):
    for i in xrange(len(grid)):
        print grid[i]
        
def gridCopy(grid):
    newGrid = []
    for i in xrange(len(grid)):
        newGrid.append([])
        for j in xrange(len(grid[i])):
            newGrid[i].append(grid[i][j])
    return newGrid

def sameGrid(g1, g2):
    for i in xrange(9):
        for j in xrange(9):
            if g1[i][j] != g2[i][j]:
                return False
    return True

def checkGrid(grid):
    h = [] #horizontal
    v = [] #vertical
    g = [] #grids
    f = [] #flags for choices
    loner = False
    counts = []
    isComplete = False
    
    #initialization
    for i in xrange(9):
        h.append(set())
        v.append(set())
        g.append(set())
        f.append([])
        counts.append(0)
        for j in xrange(9):
            f[i].append(set())
    
    for i in xrange(9):
        for j in xrange(9):
            k = grid[i][j]
            if grid[i][j] != 0:
                h[i].add(k)
                v[j].add(k)
                g[(i/3)*3+(j/3)].add(k)
                counts[k-1] += 1
    
    counts.extend(map(lambda x: len(x), h))
    counts.extend(map(lambda x: len(x), v))
    counts.extend(map(lambda x: len(x), g))
    if set(counts) == set([9]):
        isComplete = True
    
    for i in xrange(9):
        for j in xrange(9):
            if grid[i][j] == 0:
                for k in xrange(1, 10):
                    if k not in h[i]:
                        if k not in v[j]:
                            if k not in g[(i/3)*3+(j/3)]:
                                f[i][j].add(k)
                if len(f[i][j]) == 1:
                    loner = True

    return (f, loner, isComplete, counts)

def nakedSingles(grid):
    loner = checkGrid(grid)[1]
    while loner:
        newGrid = gridCopy(grid)
        f = checkGrid(grid)[0]
        for i in xrange(9):
            for j in xrange(9):
                if len(f[i][j]) == 1:
                    n = list(f[i][j])[0]
                    #print "Placed %d in (%d, %d)" % (n, i, j)
                    newGrid[i][j] = n
        grid = gridCopy(newGrid)
        loner = checkGrid(grid)[1]
    return grid

def hiddenSingles(grid):
    f = checkGrid(grid)[0]
    newGrid = gridCopy(grid)
    for i in xrange(9):
        for j in xrange(9):
            fRow = set()
            tj = range(9)
            tj.remove(j)
            for nj in tj:
                for item in list(f[i][nj]):
                    fRow.add(item)
            fCol = set()
            ti = range(9)
            ti.remove(i)
            for ni in ti:
                for item in list(f[ni][j]):
                    fCol.add(item)
            fGrid = set()
            for ni in xrange(i/3*3, i/3*3+3):
                for nj in xrange(j/3*3, j/3*3+3):
                    if not (ni == i and nj == j):
                        for item in list(f[ni][nj]):
                            fGrid.add(item)
            for n in list(f[i][j]):
                if (n not in fRow) or (n not in fCol) or (n not in fGrid):
                    #print "Placed %d in (%d, %d)" % (n, i, j)
                    newGrid[i][j] = n
    grid = gridCopy(newGrid)
    return grid

def solveRec(grid, i, j):
    #print "Recursive (%d, %d)" % (i, j)
    f = checkGrid(grid)[0]
    newGrid = gridCopy(grid)
    if len(f[i][j]) > 0:
        for n in list(f[i][j]):
            newGrid[i][j] = n
            #print "Placed %d in (%d, %d)" % (n, i, j)
            tg = solveNonRec(newGrid)
            isComplete = checkGrid(tg)[2]
            if isComplete:
                return tg
            else:
                newGrid[i][j] = 0
                continue
        grid = gridCopy(newGrid)
    if j + 1 >= 9:
        if i + 1 >= 9:
            return grid
        else:
            return solveRec(grid, i + 1, 0)
    else:
        return solveRec(grid, i, j + 1)

def solveNonRec(grid):
    oldGrid = gridCopy(grid)
    isComplete = checkGrid(grid)[2]
    while not isComplete:
        if not isComplete:
            #print "finding naked singles..."
            grid = nakedSingles(grid)
            isComplete = checkGrid(grid)[2]
        if not isComplete:
            #print "finding hidden singles..."
            grid = hiddenSingles(grid)
            isComplete = checkGrid(grid)[2]
        if sameGrid(oldGrid, grid):
            #print "Not changing"
            break
        else:
            oldGrid = gridCopy(grid)
    return grid

def solve(grid):
    grid = solveNonRec(grid)
    isComplete = checkGrid(grid)[2]
    if isComplete:
        return grid
    else:
        grid = solveRec(grid, 0, 0)
        return grid

ans = 0
for count in xrange(50):
    temp = fin.readline().strip()
    grid = []
    for i in xrange(9):
        grid.append(map(int, fin.readline().strip()))
    #print "Solving Grid", count + 1
    grid = solve(grid)
    ans += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
    #print "Done"
    #printGrid(grid)
    #print ans
print ans
