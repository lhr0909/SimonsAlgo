n = int(raw_input())
for i in xrange(n):
    x = int(raw_input())
    print reduce(lambda a, b: a * b, range(1, x+1))
