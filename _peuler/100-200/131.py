#the steps are in 131.mw
#http://d.hatena.ne.jp/inamori/20100720/p1
#http://wonderfl.net/c/1GU7/read

from MathLib import isPrime

def f(n):
    return 1 + 3 * n + 3 * n * n

ans = 0
a = 1
k = f(a)
while k < pow(10, 6):
    if isPrime(k):
        ans += 1
    a += 1
    k = f(a)

print ans