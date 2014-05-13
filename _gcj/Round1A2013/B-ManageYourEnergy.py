def dfs(E, R, N, v, prods):
    if len(prods) == len(v):
        yield sum(prods)
    else:
        s = v.pop()
        for i in xrange(E+1):
            if E-i+R >= E:
                t = E
            else:
                t = E-i+R
            dfs(t, R, N, v, prods + [s*i])


def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = 0

        E, R, N = map(int, fin.readline().strip().split(' '))
        v = map(int, fin.readline().strip().split(' '))

        print E, R, N
        print v

        for i in dfs(E, R, N, v, []):
            if i > answer:
                answer = i

        print answer
        print
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("B-tiny")
    # solve("B-small-attempt0")
    # solve("B-large")