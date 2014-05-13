c = int(raw_input().strip())
while c != 0:
    s = raw_input().strip()
    r = len(s) / c
    g = []
    #build array
    for i in xrange(r):
        t = []
        for j in xrange(c):
            t.append(' ')
        g.append(t)
    #put letters
    flip = False
    k = 0
    for i in xrange(r):
        for j in xrange(c):
            if not flip:
                g[i][j] = s[k]
            else:
                g[i][c-j-1] = s[k]
            k += 1
        flip = not flip
    #print
    result = ""
    for j in xrange(c):
        for i in xrange(r):
            result += g[i][j]
    print result
    c = int(raw_input().strip())