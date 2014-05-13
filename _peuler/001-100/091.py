def solve(n):
    count = 0
    coord = []
    for i in xrange(n+1):
        for j in xrange(n+1):
            coord.append([j, i])
    coord.pop(0)
    n = len(coord)
    s = set()
    for i in xrange(n - 1):
        p = coord[i]
        for j in xrange(1, n):
            q = coord[j]
            if p[0] == q[0] and p[0] == 0:
                #print "Same line"
                continue
            elif (p[0] != 0 and q[0] != 0) and p[1] / float(p[0]) == q[1] / float(q[0]):
                #print "Same line"
                continue
            else:
                a2 = p[0]*p[0] + p[1]*p[1]
                b2 = q[0]*q[0] + q[1]*q[1]
                dx = (p[0] - q[0])
                dy = (p[1] - q[1])
                c2 = dx*dx + dy*dy
                ab2 = a2 + b2
                bc2 = b2 + c2
                ac2 = a2 + c2
                if ab2 == c2 or bc2 == a2 or ac2 == b2:
                    t = frozenset([tuple(p), tuple(q)])
                    if t not in s:
                        #print p, q
                        s.add(t)
                        count += 1
    return count
    
print solve(50)