def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(1, T+1):
        lvls = int(fin.readline())
        reqs = []
        for i in xrange(lvls):
            reqs.append(map(int, fin.readline().strip().split(' ')) + [0])
        reqs.sort()
        if reqs[0][0] > 0:
            print "Too Bad"
            fout.write(('Case #%d: ' % case) + "Too Bad" + '\n')
            continue
        i = 0
        current = 0
        answer = 0
        while len(reqs) > 0:
            print reqs
            if reqs[i][1] <= current:
                current += (2 - reqs[i][2])
                reqs.pop(i)
                answer += 1
                continue
            elif reqs[i][0] <= current:
                current += 1
                reqs[i][2] += 1
                answer += 1
            else:
                i += 1
            if i >= len(reqs):
                i = 0
        print answer
        fout.write(('Case #%d: ' % case) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("B-small-practice")
    # solve("A-large-practice")