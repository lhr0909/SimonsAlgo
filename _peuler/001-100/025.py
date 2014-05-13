import math
digits = 1
x = 1
y = 1
n = 1000
ans = 2
while 1:
    x = x + y
    ans = ans + 1
    digits = int(math.log10(x)) + 1
    if digits>=n:
        print ans
        break
    y = x + y
    ans = ans + 1
    digits = int(math.log10(y)) + 1
    if digits>=n:
        print ans
        break
    