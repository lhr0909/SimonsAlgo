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
    
#A* this time (1min), can it be dp'ed?
class node:
    c = 0
    x = 0
    y = 0
    s = 0
    def __init__(self, nc, nx, ny, ps):
        global n
        self.c = nc
        self.x = nx
        self.y = ny
        self.s = nc + ps
    
    def __cmp__(self, other):
        if self.s < other.s:
            return -1
        elif self.s == other.s:
            return 0
        else:
            return 1
        
    def __str__(self):
        return "[%d, (%d, %d), %d]" % (self.c, self.x, self.y, self.s)

closed = set() #closed
open = [] #open
temp = node(matrix[0][0], 0, 0, 0)
open.append(temp)

while len(open) > 0:
    #print map(str, open)
    temp = open.pop(0)
    #print temp.x, temp.y
    closed.add(tuple([temp.x, temp.y]))
    if temp.x == n-1 and temp.y == n-1:
        print temp.s
        break
    for i in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nx = temp.x + i[0]
        ny = temp.y + i[1]
        if nx in range(n):
            if ny in range(n):
                if tuple([nx, ny]) not in closed:
                    newNode = node(matrix[nx][ny], nx, ny, temp.s)
                    open.append(newNode)
    open.sort()
