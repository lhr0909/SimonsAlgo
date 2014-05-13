coords = dict()

base = 0
temp = 0
while base <= 10000:
    coords[(base, base)] = temp
    temp += 1
    coords[(base + 1, base + 1)] = temp
    temp += 1
    coords[(base + 2, base)] = temp
    temp += 1
    coords[(base + 3, base + 1)] = temp
    temp += 1
    base += 2

n = int(raw_input())

for i in xrange(n):
    x, y = map(int, raw_input().strip().split(' '))
    if (x, y) in coords:
        print coords[(x, y)]
    else:
        print "No Number"