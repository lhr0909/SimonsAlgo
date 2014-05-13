a = 2
b = 0
for i in range(1901, 2001):
    for c in range(1, 13):
        if (c==4)or(c==6)or(c==9)or(c==11):
            a = a + 30
        elif c==2:
            if i % 4==0:
                a = a + 29
            else:
                a = a + 28
        else:
            a = a + 31
        if a % 7==0:
            b = b + 1
print b
