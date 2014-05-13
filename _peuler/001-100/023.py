def properdivisor(n):
    list = []
    for i in range(1,n):
        if n % i==0:
            list.append(i)
    return list

def abundantnumbers(n):
    list = []
    for i in range(12,n):
        if sum(properdivisor(i))>i:
            list.append(i)
    return list

li = abundantnumbers(28123)

newli = set()

for item1 in li:
    for item2 in li:
        if item1+item2>28123:
            break
        else:
            newli.add(item1 + item2)

print sorted(newli)[-10:]

newli2 = range(28124)

ansli = sum(list(set(newli2).difference(newli)))

print ansli
