def checkPalindrome(n):
    k = str(n)
    l = len(k)
    check = 0
    for i in range(l):
        if k[i]==k[l-i-1]:
            check += 1
    return check == l

s = set()
for i in xrange(1, 10000):
    for j in xrange(i + 1, 10001):
        temp = 0
        for k in xrange(i, j + 1):
            temp += k * k
        if temp <= pow(10, 8):
            if checkPalindrome(temp):
                print temp
                s.add(temp)
        else:
            break

print sum(s)