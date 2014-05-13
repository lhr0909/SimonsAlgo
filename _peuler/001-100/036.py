sum = 0
for i in range(1000001):
    k = 0
    temp = str(i)
    for j in range((len(temp) + 1) / 2):
        if temp[j]==temp[len(temp)-j-1]:
            k = k + 1
    if k==(len(temp) + 1) / 2:
        j = i
        temp = ''
        while j>0:
            temp = str(j % 2) + temp
            j = j / 2
        k = 0
        for j in range((len(temp) + 1) / 2):
            if temp[j]==temp[len(temp)-j-1]:
                k = k + 1
        if k==(len(temp) + 1) / 2:
            print i
            sum = sum + i
            
print sum