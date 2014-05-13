ans = 0
for b in range(100):
    for a in range(100):
        c = sum(map(int, str(a**b)))
        if c>ans:
            ans = c
print ans
