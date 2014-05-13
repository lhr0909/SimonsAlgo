def listRemove(item, ls):
    ans = []
    for i in ls:
        if i != item:
            ans.append(i)
    return ans

ans16 = []
ans17 = []
ansSet = set()
t0 = range(1, 10+1)
for a0 in t0:
    t1 = listRemove(a0, t0)
    for a1 in t1:
        t2 = listRemove(a1, t1)
        for a2 in t2:
            t3 = listRemove(a2, t2)
            for a3 in t3:
                t4 = listRemove(a3, t3)
                for a4 in t4:
                    t5 = listRemove(a4, t4)
                    for a5 in t5:
                        t6 = listRemove(a5, t5)
                        for a6 in t6:
                            t7 = listRemove(a6, t6)
                            for a7 in t7:
                                t8 = listRemove(a7, t7)
                                for a8 in t8:
                                    t9 = listRemove(a8, t8)
                                    for a9 in t9:
                                        temp = [a0, a1, a2]
                                        eq1 = a0 + a1 + a2
                                        temp += [a3, a2, a4]
                                        eq2 = a3 + a2 + a4
                                        temp += [a5, a4, a6]
                                        eq3 = a5 + a4 + a6
                                        temp += [a7, a6, a8]
                                        eq4 = a7 + a6 + a8
                                        temp += [a9, a8, a1]
                                        eq5 = a9 + a8 + a1
                                        if eq1 == eq2 and eq2 == eq3 and eq3 == eq4 and eq4 == eq5:
                                            g1 = tuple([a0, a1, a2])
                                            g2 = tuple([a3, a2, a4])
                                            g3 = tuple([a5, a4, a6])
                                            g4 = tuple([a7, a6, a8])
                                            g5 = tuple([a9, a8, a1])
                                            s = frozenset([g1, g2, g3, g4, g5])
                                            if s not in ansSet:
                                                ansSet.add(s)
                                                print temp
                                                temp = map(str, temp)
                                                temp = ''.join(temp)
                                                if len(temp) == 16: 
                                                    ans16.append(int(temp))
                                                else:
                                                    ans17.append(int(temp))
print len(ans16) + len(ans17)
print max(ans16)