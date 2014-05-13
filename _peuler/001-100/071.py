'''
def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a
    
j = 1000000
ans = [300000, 700000, 1]
while j > 999990:
    print j
    i = 430000
    while i > 428500:
        k = float(i) / float(j)
        if k > (2.0/7.0):
            if k < (3.0/7.0):
                if (3.0/7.0) - k < ans[2]:
                    ans = [i, j, (3.0/7.0) - k]
        else:
            break
        i = i - 1
    j = j - 1
print ans
'''
print 3 * 10**6 / 7 - 1

#since [3 * (100000 / 7)] / [7 * (100000 / 7)] = 428571 / 999999
#then the numerator has to be a little bit smaller than that,
#which will be 428570.
#even though, the real answer is 428570 / 999997.
