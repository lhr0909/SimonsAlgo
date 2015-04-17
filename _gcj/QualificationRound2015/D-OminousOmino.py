from multiprocessing import Pool, Manager
from copy import deepcopy
from itertools import *
import math

def solve(solve_input):
    X, R, C = solve_input

    canGabrielWin = True

    if X == 2:
        if (R * C) % 2 == 1:
            canGabrielWin = False
    elif X == 3:
        if R == 1 or C == 1 or (R * C) % 3 != 0:
            canGabrielWin = False
    elif X == 4:
        if R < 3 or C < 3 or R * C == 9:
            canGabrielWin = False

    return "GABRIEL" if canGabrielWin else "RICHARD"


def solve_file(filename, use_threadpool):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        X, R, C = map(int, fin.readline().strip().split(' '))
        inputs.append((X, R, C))
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
    solve_file("D-small-attempt2", True)
