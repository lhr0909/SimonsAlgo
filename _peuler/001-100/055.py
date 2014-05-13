def checkPalindrome(n):
    k = str(n)
    l = len(k)
    check = 0
    for i in range(l):
        if k[i]==k[l-i-1]:
            check += 1
    return check == l
    
ans = 0
for i in range(10000):
    j = 0
    k = i
    while j <= 50:
        k = k + int(str(k)[::-1])
        if checkPalindrome(k):
            break
        else:
            j += 1
    if j>50:
        ans += 1
print ans
