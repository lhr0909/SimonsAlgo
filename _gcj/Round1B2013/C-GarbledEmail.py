dict1 = open("dict.txt", "r").readlines()
dict2 = open("dict_goog.txt", "r").readlines()

wordset = set(map(lambda x: x.strip().lower(), dict1 + dict2))
del dict1
del dict2
print len(wordset)

print "Building dictionary based on length.."
d1 = dict()
for word in wordset:
    if len(word) not in d1:
        d1[len(word)] = set([word])
    else:
        d1[len(word)].add(word)

def compare_words(a, b):
    zipped = zip(a, b)
    return sum(map(lambda x: 1 if len(x) == 2 else 0, map(set, zipped)))


def solve(filename):
    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        answer = float(0)
        email = fin.readline().strip()
        print email,
        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()

if __name__ == "__main__":
    solve("C-tiny")
    # solve("C-small-attempt0")
    # solve("C-large")