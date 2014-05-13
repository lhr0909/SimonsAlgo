count = 0
set89 = set()
set1 = set()
maxSum = 7*9*9
for i in xrange(1, 10000000):
    k = i
    if i % 1000000 == 0:
        print i
    while k!=1 or k!=89:
        temp = 0
        f = k
        while f > 0:
            temp += (f%10) * (f%10)
            f /= 10
        if temp in set1:
            if i <= maxSum:
                set1.add(i)
            break
        elif temp in set89:
            if i <= maxSum:
                set89.add(i)
            count += 1
            break
        elif temp==1:
            if i <= maxSum:
                set1.add(i)
            break
        elif temp==89:
            if i <= maxSum:
                set89.add(i)
            count += 1
            break
        else:
            k = temp

print count
