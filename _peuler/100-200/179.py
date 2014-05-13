from Maple import *

maple = Maple()
openNumTheory(maple)

s = 0

for i in xrange(2, pow(10, 7)):
    if i % pow(10, 5) == 0:
        print i, s
    a = int(maple.execute('tau(%d)' % i))
    b = int(maple.execute('tau(%d)' % (i+1)))
    if a == b:
        s += 1
print s
del maple