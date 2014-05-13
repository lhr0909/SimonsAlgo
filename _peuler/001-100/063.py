ans = 0
for i in range(1, 25):
    j = 1
    while j<10:
        if len(str(pow(j,i)))==i:
            ans += 1
            #print "%d^%d = %d" % (j, i, pow(j, i))
            j += 1
        elif len(str(pow(j,i)))>i:
            break
        else:
            j += 1

print ans
