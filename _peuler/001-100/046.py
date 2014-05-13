from math import sqrt

def sieve(n):
    li = [True] * n
    li[0] = False
    li[1] = False
    for i in range(2, n):
        if li[i]:
            for j in range(i*i, n, i):
                li[j] = False
    return li

table = sieve(6000)
for i in range(3, 6000):
    if (not table[i]) and i % 2 == 1:
        flag = False
        for j in range(i, 1, -1):
            if table[j]:
                checkSquare = sqrt((i-j) / 2)
                if checkSquare == int(checkSquare):
                    flag = True
                    #print "%d = %d + 2 * %d^2" % (i, j, int(checkSquare))
                    break
        if not flag:
            print i
            break
                    
