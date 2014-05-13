file = open('022.txt','r').read().replace('"','').split(',')
file.sort()
total = 0
for i in range(len(file)):
    score = 0
    for j in range(len(file[i])):
        score = score + ord(file[i][j]) - ord('A') + 1
    score = score * (i + 1)
    total = total + score
print total
