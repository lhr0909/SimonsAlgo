n = 80
matrix = [row.split(',') for row in open('081-083.txt', 'r').read().split('\r\n')[:-1]]

'''
n = 5
matrix = [['131', '673', '234', '103', '18'],
          ['201', '96', '342', '965', '150'],
          ['630', '803', '746', '422', '111'],
          ['537', '699', '497', '121', '956'],
          ['805', '732', '524', '37', '331']]
'''

matrix = [map(int, row) for row in matrix]

c = []
for i in xrange(n):
    temp = []
    for j in xrange(n):
        temp.append(0)
    c.append(temp)

for i in xrange(n):
    c[i][0] = matrix[i][0]
    
for j in xrange(n):
    for i in xrange(n):
        c[i][j] = matrix[i][j]
        if j > 0:
            minArray = []
            for k in xrange(n):
                temp = c[k][j-1]
                if k < i:
                    temp += sum([matrix[l][j] for l in xrange(k, i)])
                elif k > i:
                    temp += sum([matrix[l][j] for l in xrange(i+1, k+1)])
                minArray.append(temp)
            c[i][j] += min(minArray)

'''
for i in xrange(n):
    print c[i]
'''

print min([c[i][n-1] for i in xrange(n)])