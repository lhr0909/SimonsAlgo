n = int(raw_input())
for i in xrange(n):
    x, y = raw_input().strip().split(' ')
    print reduce(lambda a, b: int(str(int(a[::-1]) + int(y[::-1]))[::-1]), [x, y])
