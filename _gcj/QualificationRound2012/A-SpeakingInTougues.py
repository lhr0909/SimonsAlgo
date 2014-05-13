#brute force the fuck out of this
words = dict()

words[' '] = ' '
words['a'] = 'y'
words['b'] = 'h'
words['c'] = 'e'
words['d'] = 's'
words['e'] = 'o'
words['f'] = 'c'
words['g'] = 'v'
words['h'] = 'x'
words['i'] = 'd'
words['j'] = 'u'
words['k'] = 'i'
words['l'] = 'g'
words['m'] = 'l'
words['n'] = 'b'
words['o'] = 'k'
words['p'] = 'r'
words['q'] = 'z'
words['r'] = 't'
words['s'] = 'n'
words['t'] = 'w'
words['u'] = 'j'
words['v'] = 'p'
words['w'] = 'f'
words['x'] = 'm'
words['y'] = 'a'
words['z'] = 'q'

def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    N = int(fin.readline())
    for case in xrange(1, N+1):
        message = fin.readline()[:-1]
        result_list = [words[letter] for letter in message]
        fout.write(('Case #%d: ' % case) + ''.join(result_list) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("A-small-practice")