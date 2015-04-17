from multiprocessing import Pool, Manager
from copy import deepcopy
from itertools import *

def solve(solve_input):
    Smax, S = solve_input
    S = map(int, S[:])

    fNeeded = 0
    fStoodUp = S[0]
    for i in xrange(1, len(S)):
        if S[i] > 0:
            if fStoodUp < i:
                friends_needed = i - fStoodUp
                fNeeded += friends_needed
                fStoodUp += friends_needed + S[i]
            else:
                fStoodUp += S[i]

    return fNeeded


def solve_file(filename, use_threadpool):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        Smax, S = fin.readline().strip().split(' ')
        inputs.append((int(Smax), S))
    #solve
    answers = []
    if use_threadpool:
        thread_pool = Pool(10)
        answers = thread_pool.map(solve, inputs)
    else:
        answers = map(solve, inputs)
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answers[i-1]) + "\n")

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve_file("A-large", True)
