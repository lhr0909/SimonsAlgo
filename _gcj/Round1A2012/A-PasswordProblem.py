from itertools import *

def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(1, T+1):
        A, B = map(int, fin.readline().strip().split(' '))
        P = map(float, fin.readline().strip().split(' '))
        PComplete = [((x, True), (1.0 - x, False)) for x in P]
        print PComplete
        TotalP = map(lambda x: reduce(lambda x, y: x[0] * y[0] if type(x) == tuple else x * y[0], x), list(product(*PComplete)))
        print TotalP
        for i in product(*PComplete):
            print i, reduce(lambda x, y: x[0] * y[0] if type(x) == tuple else x * y[0], i)
        #fout.write(('Case #%d: ' % case) + str(answer) + '\n')
        print

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("A-small-practice")
    # solve("A-large-practice")