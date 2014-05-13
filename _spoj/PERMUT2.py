#http://mathworld.wolfram.com/InversePermutation.html
#An inverse permutation is a permutation in which each number and the number of the place which it occupies are exchanged

n = int(raw_input())
while n > 0:
    perm_str = raw_input().strip()
    #had to build this into a hash table for fixing TLE
    perm = dict(zip(map(int, perm_str.split(' ')), range(1, n + 1)))
    inv_perm = tuple([perm[x] for x in xrange(1, len(perm) +1)])
    #print " ".join(map(str, inv_perm))
    if " ".join(map(str, inv_perm)) == perm_str:
        print "ambiguous"
    else:
        print "not ambiguous"
    n = int(raw_input())