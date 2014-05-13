import sys
import itertools
import time

sys.setrecursionlimit(200)


def recursion(N, chests, keys, results):
    # print chests
    # print keys
    # print results
    # print
    if len(chests) == 0:
        if len(results) == N:
            # Right Answer
            return results
        else:
            # Wrong Answer
            return []
    else:
        first_chests = sorted(filter(lambda c: c[1] in keys, chests))
        i = 0
        removed = False
        while i < len(first_chests):
            c = first_chests[i]
            next_chests = chests.copy()
            next_chests.remove(c)
            next_keys = keys[:]
            next_keys.remove(c[1])
            next_keys.extend(c[2])
            next_results = results + [c]
            next_recursion = recursion(N, next_chests, next_keys, next_results)
            if next_recursion is not None:
                return next_recursion
            i += 1
        return None


def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        print case + 1
        K, N = map(int, fin.readline().strip().split(' '))
        keys = map(int, fin.readline().strip().split(' '))
        chests = set()
        for i in xrange(N):
            chest = map(int, fin.readline().strip().split(' '))
            chests.add((i + 1, chest[0], tuple(chest[2:])))

        # DFS
        result = recursion(N, chests, keys, [])

        if result is None or len(result) == 0:
            # print "no solution"
            answer = "IMPOSSIBLE"
        else:
            answer = ' '.join(map(lambda c: str(c[0]), result))

        print "Case #%d: " % (case + 1), answer
        print
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()


if __name__ == "__main__":
    # solve("D-tiny")
    solve("D-small-attempt2")
    # solve("D-large")