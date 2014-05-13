#UAD Trees for Pythagorean Triples
#http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Pythag/pythag.html#uadgen
#http://mathworld.walfram.com/PythagoreanTriple.html

r = dict()
q = []

q.append([3, 4, 5])

#get all primitive pythagorean triples
while len(q) > 0:
    a, b, h = q.pop(0)
    k = a + b + h
    if k <= 1500000:
        #print a, b, h
        if k not in r:
            r[k] = set()
        r[k].add(tuple(sorted([a, b, h])))
        #go UP
        q.append([a-2*b+2*h, 2*a-b+2*h, 2*a-2*b+3*h])
        #go ALONG
        q.append([a+2*b+2*h, 2*a+b+2*h, 2*a+2*b+3*h])
        #go DOWN
        q.append([(-a)+2*b+2*h, (-2*a)+b+2*h, (-2*a)+2*b+3*h])

#generate the rest based on the primitives
primitives = r.keys()
for v in primitives:
    count = 2
    for i in xrange(v+v, 1500000, v):
        if i not in r:
            r[i] = set()
        for triple in list(r[v]):
            a, b, h = triple
            a, b, h = a*count, b*count, h*count
            r[i].add(tuple([a, b, h]))
        count += 1

#count the ones with only one triple
ans = 0
for i in r.keys():
    if len(r[i]) == 1:
        ans += 1
print ans
