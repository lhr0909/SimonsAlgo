from multiprocessing import Pool, Manager
from itertools import *
from copy import deepcopy

def check_train(s):
    dup_set = set()
    last_letter = ""
    for i in xrange(len(s)):
        letter = s[i]
        if last_letter == "":
            last_letter = letter
            dup_set.add(letter)
        elif letter != last_letter:
            if letter not in dup_set:
                last_letter = letter
                dup_set.add(letter)
            else:
                return False
    return True

def solve(solve_input):
    carts = tuple(sorted(solve_input))
    count = 0
    for perm in permutations(carts):
        s = ''.join(perm)
        if check_train(s):
            count += 1
    return count

def solve_file(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        N = int(fin.readline())
        carts = fin.readline().strip().split(' ')
        inputs.append(carts)
    #solve
    thread_pool = Pool(10)
    answers = thread_pool.map(solve, inputs)
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answers[i-1]) + "\n")

    fin.close()
    fout.close()

if __name__ == '__main__':
    solve_file("B-small-attempt0")
