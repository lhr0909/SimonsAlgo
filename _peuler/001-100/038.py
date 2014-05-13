li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 0
for i in range(1,10000):
    temp = ""
    for number in li:
        temp += str(i*number)
        if len(temp)>=9:
            break
    if len(temp)>9:
        continue
    else:
        flag = [False, False, False, False, False, False, False, False, False]
        for digit in temp:
            flag[int(digit)-1] = True
        flagCount = 0
        for flags in flag:
            if flags:
                flagCount = flagCount + 1
        if flagCount==9:
            if int(temp)>m:
                m = int(temp)

print m
    
