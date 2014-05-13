from math import factorial

i = 11
ans = []
while i<=40585:
    if sum(factorial(int(digit)) for digit in str(i))==i:
        ans.append(i)
    i = i + 1
print sum(ans)