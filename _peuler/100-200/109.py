singles = ['0'] + map(lambda x: 'S%d' % x, range(1, 21)) + ['S25']
doubles = ['0'] + map(lambda x: 'D%d' % x, range(1, 21)) + ['D25']
triples = ['0'] + map(lambda x: 'T%d' % x, range(1, 21))
fDoubles = map(lambda x: 'D%d' % x, range(1, 21)) + ['D25']

d = dict()

def translate(t):
    if t == '0':
        return 0
    else:
        x = t[0]
        y = t[1:]
        if x == 'S':
            return int(y)
        elif x == 'D':
            return 2 * int(y)
        elif x == 'T':
            return 3 * int(y)
    

i = 0
while i < 65:
    if i < 22:
        t1 = singles[i]
    elif i >= 22 and i < 44:
        t1 = doubles[i - 22]
    elif i >= 44 and i < 65:
        t1 = triples[i - 44]
    j = 0
    while j < 65:
        if j < 22:
            t2 = singles[j]
        elif j >= 22 and j < 44:
            t2 = doubles[j - 22]
        elif j >= 44 and j < 65:
            t2 = triples[j - 44]
        for k in xrange(len(fDoubles)):
            t3 = fDoubles[k]
            s = (tuple(sorted([t1, t2])), t3)
            p = translate(t1) + translate(t2) + translate(t3)
            if p not in d:
                d[p] = set([s])
            else:
                d[p].add(s)
        j += 1
    i += 1

ans = 0

for i in sorted(d.keys()):
    if i < 100:
        ans += len(d[i])
        #print i, len(d[i])
    
print ans