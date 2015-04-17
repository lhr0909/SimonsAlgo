from multiprocessing import Pool, Manager
from copy import deepcopy
from itertools import *
import math

def mul_s(s1, s2):
    d = {
        "ii": "-1",
        "jj": "-1",
        "kk": "-1",
        "ij": "k",
        "ji": "-k",
        "jk": "i",
        "kj": "-i",
        "ik": "-j",
        "ki": "j",
        "1i": "i",
        "i1": "1",
        "1j": "j",
        "j1": "j",
        "1k": "k",
        "k1": "k",
        "11": "1"
    }

    if s1[0] == "-":
        if s2[0] == "-":
            return d[s1[1] + s2[1]]
        else:
            if d[s1[1] + s2][0] == "-":
                return d[s1[1] + s2][1:]
            else:
                return "-" + d[s1[1] + s2]
    else:
        if s2[0] == "-":
            if d[s1 + s2[1]][0] == "-":
                return d[s1 + s2[1]][1:]
            else:
                return "-" + d[s1 + s2[1]]
        else:
            return d[s1 + s2]

def eval_s(s, d):
    if s not in d:
        if len(s) <= 1:
            d[s] = s[0]
        elif len(s) == 2:
            d[s] = mul_s(s[0], s[1])
        else:
            top_half = s[:len(s) / 2]
            bottom_half = s[len(s) / 2:]
            d[s] = mul_s(
                eval_s(tuple(top_half), d),
                eval_s(tuple(bottom_half), d)
            )
    return d[s]

def each_substring_partition(s, n, d):
    i = 1

    while i < n - 1:
        j = 1
        while j < n - i:
            si = s[:i]
            sj = s[i:i+j]
            sk = s[i+j:]

            yield (
                eval_s(tuple(si), d),
                eval_s(tuple(sj), d),
                eval_s(tuple(sk), d)
            )

            j += 1
        i += 1

def pre_processing(s):
    print len(s)
    loc = 0
    length = 0
    letter = ""
    i = 0
    while i < len(s):
        if s[i] != letter:
            letter = s[i]
            loc = i
            length = 0
        else:
            length += 1
            if length >= 4:
                s = s[:loc] + s[loc+length:]
            else:
                i += 1
    print len(s)
    return s

def solve(solve_input):
    solve_input, d = solve_input
    L, X, s = solve_input
    s = pre_processing(s * X)

    answer = False

    if L > 1 and len(set(s)) > 1 and L * X >= 3:
        for (i, j, k) in each_substring_partition(s, L * X, d):
            if (i == "i") and (j == "j") and (k == "k"):
                answer = True
                break

    return "YES" if answer else "NO"


def solve_file(filename, use_threadpool):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')
    #data read
    inputs = []
    T = int(fin.readline())
    for case in xrange(T):
        L, X = map(int, fin.readline().strip().split(' '))
        s = fin.readline().strip()
        inputs.append((L, X, s))
    #solve
    answers = []
    manager = Manager()
    d = manager.dict()
    dd = dict()
    if use_threadpool:
        thread_pool = Pool(10)
        answers = thread_pool.map(solve, map(lambda x: (x, d), inputs))
    else:
        answers = map(solve, map(lambda x: (x, dd), inputs))
    #output
    for i in xrange(1, len(answers) + 1):
        fout.write(("Case #%d: " % i) + str(answers[i-1]) + "\n")

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve_file("C-small-attempt0", True)
