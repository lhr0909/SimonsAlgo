#add and mod, should be cyclic. Awesome educated guess.
#extensive reading:
#http://mathworld.wolfram.com/TribonacciNumber.html

def nonDivisor(n):
    s = [1, 1, 1, 3, 5, 9]
    
    i = 6
    while True:
        s.append((s[i-1] + s[i-2] + s[i-3]) % n)
        if s[i-3] == 1 and s[i-2] == 1 and s[i-1] == 1:
            return True
        elif s[i] == 0:
            return False
        i += 1

count = 0
i = 27
while count < 124:
    if nonDivisor(i):
        count += 1
        print i, count
    i += 2