#faster way
cubes = [sorted(map(int, str(i**3))) for i in xrange(10000)]
for i in cubes:
    if cubes.count(i) == 5:
        print cubes.index(i)**3
        break
#my way:
'''cubes = []
for i in xrange(10000):
    temp = {}
    for digit in str(i**3):
        if temp.has_key(digit):
            temp[digit] += 1
        else:
            temp[digit] = 1
    cubes.append(temp)

for i in xrange(9999):
    k = 0
    for j in xrange(i+1, 10000):
        if cubes[i]==cubes[j]:
            if len(str(i**3))==len(str(j**3)):
                #print "%d^3 = %d, %d^3 = %d" % (i, i**3, j, j**3)
                k = k + 1
    if k == 4:
        print i, i**3
        #print
        break
'''
