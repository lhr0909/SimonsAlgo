from itertools import *

def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = None
        #data read
        N, L = map(int, fin.readline().strip().split(" "))
        #print N, L
        outlets = map(lambda x: int(x, 2), fin.readline().strip().split(" "))
        devices = map(lambda x: int(x, 2), fin.readline().strip().split(" "))
        # print outlets, devices
        if (frozenset(outlets) == frozenset(devices)):
            answer = 0
        else:
            for flip_bits in xrange(1, 2**L):
                new_outlets = map(lambda x: x ^ flip_bits, outlets)
                #print indices, new_outlets, devices
                if (frozenset(new_outlets) == frozenset(devices)):
                    answer = list("{0:#b}".format(flip_bits)).count("1")
                    break
        if answer is None:
            answer = "NOT POSSIBLE"
        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("A-small-practice")
