def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(1, T+1):
        test_case = fin.readline().strip().split(' ')
        N = int(test_case[0])
        S = int(test_case[1])
        p = int(test_case[2])
        t = sorted(map(int, test_case[3:]), reverse=True)
        #print N, S, p, t
        answer = 0
        for score in t:
            avg = score / 3
            if avg >= p:
                #accept this case
                answer += 1
                continue
            else:
                remaining = score - avg * 3
                #print avg, remaining
                if remaining >= 1 and avg + 1 >= p:
                    answer += 1
                elif S > 0:
                    if remaining == 0 and avg != 0 and avg + 1 >= p:
                        S -= 1
                        answer += 1
                    elif remaining == 1 and avg + 1 >= p:
                        S -= 1
                        answer += 1
                    elif remaining == 2 and avg + 2 >= p:
                        S -= 1
                        answer += 1
        #print answer
        fout.write(('Case #%d: ' % case) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("B-small-practice")
    solve("B-large-practice")