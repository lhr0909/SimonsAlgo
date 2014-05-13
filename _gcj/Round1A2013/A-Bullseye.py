from math import sqrt

def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = 0
        r, t = map(int, fin.readline().strip().split(' '))

        # sum((r+2*k-1)^2 - (r+2*k-2)^2, k=1..n) = 2*r(n+1) - 5*n - 2 + 2*(n+1)^2 - 2*r
        # solve 2*r(n+1) - 5*n - 2 + 2*(n+1)^2 - 2*r = t for n
        # n = -r/2 + 1/4 +- 1/4*sqrt(4*r^2 - 4*r + 1 + 8*t)

        s1 = -r / float(2) + 0.25 + 0.25 * sqrt(4*r*r - 4*r + 1 + 8*t)
        s2 = -r / float(2) + 0.25 - 0.25 * sqrt(4*r*r - 4*r + 1 + 8*t)

        answer = int(s1) if s1 > 0 else int(s2)

        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    # solve("A-tiny")
    # solve("A-small-attempt0")
    solve("A-large")