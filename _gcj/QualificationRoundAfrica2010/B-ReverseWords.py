def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    N = int(fin.readline())
    for case in xrange(1, N+1):
        words = fin.readline().strip().split(' ')
        words.reverse()
        fout.write(('Case #%d: ' % case) + ' '.join(words) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("B-small-practice")
    solve("B-large-practice")