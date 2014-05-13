# http://www.purplemath.com/modules/factzero.htm

n = int(raw_input())
for i in xrange(n):
    x = int(raw_input())
    zeroes = 0
    j = 5
    fives = x / j
    while fives >= 1:
        zeroes += fives
        j *= 5
        fives = x / j
    print zeroes