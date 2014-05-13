def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = ""
        #data read
        row1 = int(fin.readline()) - 1
        board1 = []
        for i in xrange(4):
            board1.append(map(int, fin.readline().strip().split(' ')))
        row2 = int(fin.readline()) - 1
        board2 = []
        for i in xrange(4):
            board2.append(map(int, fin.readline().strip().split(' ')))

        #check intersection of two row sets
        overlap = set(board1[row1]) & set(board2[row2])
        if len(overlap) == 1:
            answer = list(overlap)[0]
        elif len(overlap) == 0:
            answer = "Volunteer cheated!"
        else:
            answer = "Bad magician!"

        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("A-small-attempt0")