from multiprocessing import Pool
from itertools import *
from copy import deepcopy

def solve(solve_input):
    P, Q = solv_input
    return "%s + %s"

def solve_file(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        P, Q = map(int, fin.readline().strip().split('/'))
        inputs.append((P, Q))
    #solve
    thread_pool = Pool(5)
    answers = thread_pool.map(solve, inputs)
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answer))

    fin.close()
    fout.close()

if __name__ == '__main__':
    solve_file("A-large")
