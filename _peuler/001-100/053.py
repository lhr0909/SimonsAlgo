def makeBinomial(row):
    table = [[0 for j in range(i)] for i in range(1,row+1)]
    for i in range(row):
        table[i][0] = 1
        table[i][i] = 1
        if i>1:
            for j in range(1, i):
                table[i][j] = table[i-1][j-1] + table[i-1][j]
    return table
    
count = 0
t = makeBinomial(101)
for i in range(23, 101):
    for j in range(i):
        if t[i][j]>10**6:
            count += 1
            
print count
