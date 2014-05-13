n = 80
matrix = [row.split(',') for row in open('081-083.txt', 'r').read().split('\r\n')[:-1]]
'''
matrix = [['131', '673', '234', '103', '18'],
          ['201', '96', '342', '965', '150'],
          ['630', '803', '746', '422', '111'],
          ['537', '699', '497', '121', '956'],
          ['805', '732', '524', '37', '331']]
'''
for i in xrange(n-1, -1, -1):
    for j in xrange(n-1, -1, -1):
        if i==n-1:
            if j==n-1:
                matrix[i][j] = int(matrix[i][j])
            else:
                matrix[i][j] = int(matrix[i][j]) + int(matrix[i][j+1])
        else:
            if j==n-1:
                matrix[i][j] = int(matrix[i][j]) + int(matrix[i+1][j])
            else:
                matrix[i][j] = int(matrix[i][j]) + min(int(matrix[i+1][j]), int(matrix[i][j+1]))
        
print matrix[0][0]
