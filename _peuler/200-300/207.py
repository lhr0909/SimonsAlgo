#Got fucked by the statement: concentrated on the power t too much.
'''
4^t = 2^t + k
let x = 2^t
4^t = x^2
x^2 = x + k

loop through x (start from 2), and you can find x^2 and k.
'''
lastX = 2
x = 2
numerator = 1
denominator = 1
while denominator / numerator <= 7000:
    x *= 2
    numerator += 1
    denominator += (x - lastX)
    lastX = x

while numerator / float(denominator) >= 1 / float(12345):
    x += 1
    denominator += 1

#print x
#print denominator / numerator
k = x*x - x
print k