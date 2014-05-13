from multiprocessing import Pool, Manager
from itertools import *
from copy import deepcopy
from fractions import Fraction
from decimal import Decimal
import math

#(A/B + C/D) / 2 = (AD + CB) / 2 /BD

def is_int(x):
    return abs(math.ceil(x) - x) < 0.00000001

def solve(solve_input):
    P, Q = solve_input
    frac = Fraction(P, Q)
    numer, denom = (frac.numerator, frac.denominator)
    log_denom = math.log(denom, 2)
    if is_int(log_denom):
        i = 1
        while frac - Fraction(1, i) < 0:
            i <<= 1
        return int(math.log(i, 2))
    else:
        return "impossible"

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
    thread_pool = Pool(10)
    answers = thread_pool.map(solve, inputs)
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answers[i-1]) + "\n")

    fin.close()
    fout.close()

if __name__ == '__main__':
    solve_file("A-large")
