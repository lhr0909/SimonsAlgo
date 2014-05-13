ans = []
for i in range(12,100):
    for j in range(i+1,100):
        if (i%11==0)or(i%10==0)or(j%11==0)or(j%10==0):
            continue
        val1 = float(str(i) + '.0') / float(str(j) + '.0')
        for digit1 in str(i):
            for digit2 in str(j):
                if digit1==digit2:
                    tempi = str(i).replace(digit1,"")
                    tempj = str(j).replace(digit2,"")
                    val2 = float(tempi + '.0') / float(tempj + '.0')
                    if val1==val2:
                        ans.append([i,j])
                        break
numerator = 1
denominator = 1
for term in ans:
    numerator = numerator * term[0]
    denominator = denominator * term[1]

print "Answer:", denominator / numerator