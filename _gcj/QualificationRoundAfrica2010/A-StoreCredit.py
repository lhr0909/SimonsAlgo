def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    N = int(fin.readline())
    for case in xrange(1, N+1):
        #print case
        C = int(fin.readline())
        I = int(fin.readline())
        items = map(int, fin.readline().split(' '))
        #print C
        itemset = set(items)
        itemset_subtract = set(map(lambda x: C - x, items))
        #since there is only one solution in every case, intersection will work
        intersect = itemset.intersection(itemset_subtract)
        # if the value is exact half,
        # need to delete if there is only one of that number in the item list,
        # as it will always be in the intersection
        if len(intersect) % 2 == 1:
            for item in intersect:
                if item * 2 == C and items.count(item) == 1:
                    intersect.remove(item)
                    break
        #print intersect
        #get indices
        indices = ["%d" % (i+1) for i, x in enumerate(items) if x in intersect]
        fout.write(('Case #%d: ' % case) + ' '.join(indices) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("A-small-practice")
    solve("A-large-practice")