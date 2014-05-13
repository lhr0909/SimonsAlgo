def listRemove(item, ls):
    ans = []
    for i in ls:
        if i != item:
            ans.append(i)
    return ans

def calc(ls1):
    seq = set()
    operator = ['+', '-', '*', '/']
    exp = []
    exp.append("a o1 b o2 c o3 d")
    exp.append("(a o1 b) o2 c o3 d")
    exp.append("(a o1 b o2 c) o3 d")
    exp.append("((a o1 b) o2 c) o3 d")
    exp.append("(a o1 (b o2 c)) o3 d")
    exp.append("a o1 (b o2 c) o3 d")
    exp.append("a o1 (b o2 c o3 d)")
    exp.append("a o1 ((b o2 c) o3 d)")
    exp.append("a o1 (b o2 (c o3 d))")
    exp.append("a o1 b o2 (c o3 d)")
    exp.append("(a o1 b) o2 (c o3 d)")
    for i in operator:
        for j in operator:
            for k in operator:
                for l in exp:
                    e = l.replace('o1', i).replace('o2', j).replace('o3', k)
                    for a in ls1:
                        ls2 = listRemove(a, ls1)
                        for b in ls2:
                            ls3 = listRemove(b, ls2)
                            for c in ls3:
                                ls4 = listRemove(c, ls3)
                                for d in ls4:
                                    try:
                                        t = eval(e)
                                    except ZeroDivisionError:
                                        continue
                                    if t == int(t) and t > 0:
                                        seq.add(int(t))
    ans = list(seq)
    i = 1
    while i <= len(ans):
        if ans[:i] != range(1, i+1):
            break
        i += 1
    return i - 1

longest = 0
ans = ""
for d in xrange(1, 10):
    for c in xrange(1, d):
        for b in xrange(1, c):
            for a in xrange(1, b):
                t = map(float, [a, b, c, d])
                k = calc(t)
                if k > longest:
                    longest = k
                    ans = str(a) + str(b) + str(c) + str(d)
                    print longest, ans
print ans
