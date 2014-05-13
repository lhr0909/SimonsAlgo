'''=======================my solution=================
def rem(a, n):
    return (pow(a-1, n, a*a) + pow(a+1, n, a*a)) % (a*a)

rmax = []

for i in xrange(3, 1001):
    temp = set()
    for j in xrange(1, 2 * i + 1):
        k = rem(i, j)
        temp.add(k)
    if i == 7:
        print max(temp)
    rmax.append(max(temp))

print sum(rmax)
'''

'''
This was a very quick one: (a+1)^n == an+1 (mod a^2),
and (a-1)^n == an-1 or 1-an (mod a^2) depending whether n is odd or even;
the sum is therefore either 2an or 2.

When a is odd, this is always maximised at a^2-a (as in the example with a=7),
achieved for example when n=(a-1)/2;
when a is even, it is maximised at a^2-2a for a>2,
achieved for example when n=(a-2)/2. 
'''

s = 0

for a in xrange(3, 1001):
    if a % 2 == 1:
        s += a * a - a
    else:
        s += a * a - 2 * a

print s
