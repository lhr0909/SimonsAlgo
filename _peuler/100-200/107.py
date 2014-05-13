#matrix = "-,16,12,21,-,-,-\r\n16,-,-,17,20,-,-\r\n12,-,-,28,-,31,-\r\n21,17,28,-,18,19,23\r\n-,20,-,18,-,-,11\r\n-,-,31,19,-,-,27\r\n-,-,-,23,11,27,-"
matrix = open("107.txt", "r").read()[:-2]
matrix = matrix.split('\r\n')
matrix = map(lambda x: x.split(','), matrix)

numV = len(matrix)

original = 0

for i in xrange(numV):
    for j in xrange(i):
        if matrix[i][j] != '-':
            original += int(matrix[i][j])

edges = []
s1 = set(range(1, numV))
s2 = set([0])

while s1 != set():
    m = pow(2, 32)
    sP = 0
    eP = 0
    for v in s2:
        for u in s1:
            if matrix[v][u] != '-':
                k = int(matrix[v][u])
                if k < m:
                    m = k
                    sP = v
                    eP = u
    edges.append(tuple([sP, eP]))
    s1.remove(eP)
    s2.add(eP)

saved = 0
for edge in edges:
    saved += int(matrix[edge[0]][edge[1]])

print original - saved

#http://en.wikipedia.org/wiki/Prim%27s_algorithm

#better one
#http://en.wikipedia.org/wiki/Kruskal%27s_algorithm