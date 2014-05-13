#love yield from now on!
from MathLib import choose_iter

def checkCube(c1, c2):
    s = set()
    for n1 in c1:
        for n2 in c2:
            if n1 == 6 or n1 == 9:
                k1 = [6, 9]
            else:
                k1 = [n1]
            if n2 == 6 or n2 == 9:
                k2 = [6, 9]
            else:
                k2 = [n2]
            for m1 in k1:
                for m2 in k2:
                    s.add(m1 * 10 + m2)
                    s.add(m2 * 10 + m1)
    for i in [1, 4, 9, 16, 25, 36, 49, 64, 81]:
        if i not in s:
            return False
    return True

count = 0
for c1 in choose_iter(range(10), 6):
    for c2 in choose_iter(range(10), 6):
        if checkCube(c1, c2):
            print c1, c2
            count += 1

print count / 2 #deadly duplicates!!!