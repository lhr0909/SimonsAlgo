t9dict = dict()

t9dict[' '] = '0'
t9dict['a'] = '2'
t9dict['b'] = '22'
t9dict['c'] = '222'
t9dict['d'] = '3'
t9dict['e'] = '33'
t9dict['f'] = '333'
t9dict['g'] = '4'
t9dict['h'] = '44'
t9dict['i'] = '444'
t9dict['j'] = '5'
t9dict['k'] = '55'
t9dict['l'] = '555'
t9dict['m'] = '6'
t9dict['n'] = '66'
t9dict['o'] = '666'
t9dict['p'] = '7'
t9dict['q'] = '77'
t9dict['r'] = '777'
t9dict['s'] = '7777'
t9dict['t'] = '8'
t9dict['u'] = '88'
t9dict['v'] = '888'
t9dict['w'] = '9'
t9dict['x'] = '99'
t9dict['y'] = '999'
t9dict['z'] = '9999'

def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    N = int(fin.readline())
    for case in xrange(1, N+1):
        message = fin.readline()[:-1]
        #convert each letter into key presses
        result_list = [t9dict[letter] for letter in message]
        #deal with the pauses
        result = ""
        for item in result_list:
            if len(result) > 0 and result[-1] == item[0]:
                result += (" " + item)
            else:
                result += item
        fout.write(('Case #%d: ' % case) + result + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("C-small-practice")
    solve("C-large-practice")