from multiprocessing import Pool, Manager
from copy import deepcopy
from itertools import *

def choose(n, r, d):
    if r > n or n <= 0 or r <= 0 or r == n:
        return 1
    else:
        if (n, r) not in d:
            d[(n, r)] = choose(n - 1, r - 1, d) + choose(n - 1, r, d)
        return d[(n, r)]


def solve(solve_input):
    solve_input, memoize_dict = solve_input
    n, r = solve_input
    answer = choose(n, r, memoize_dict)
    return answer

def solve_file(filename, use_threadpool):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        n, r = map(int, fin.readline().strip().split(' '))
        inputs.append((n, r))
    #solve
    answers = []
    if use_threadpool:
        manager = Manager()
        memoize_dict = manager.dict()
        inputs_with_dict = map(lambda x: (x, memoize_dict), inputs)
        thread_pool = Pool(10)
        answers = thread_pool.map(solve, inputs_with_dict)
    else:
        memoize_dict = dict()
        inputs_with_dict = map(lambda x: (x, memoize_dict), inputs)
        answers = map(solve, inputs_with_dict)
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answers[i-1]) + "\n")

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve_file("template-example", True)
