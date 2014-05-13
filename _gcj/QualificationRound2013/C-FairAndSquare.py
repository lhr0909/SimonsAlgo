# http://oeis.org/A002779

# Have to use this sequence to solve the large large case without cheating
# http://oeis.org/A057135

# Let's play this number game!
# Contructing a number with "(012)^n", flip, add (nothing, 0, 1, 2), and check if its square is a palindrome.
# start from 1001, pretty much build to about 50 digits.
# Damn! still slow (15-20 minutes)


# num_set = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201,
#            104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L,
#            12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L,
#            1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L,
#            4000008000004L, 4004009004004L}
#
# num_set2 = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002,
#             20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101,
#             1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002}

import itertools

num_set2 = {1, 2, 3, 11, 22}
num_set = set(map(lambda x: x * x, num_set2))


def isPalindrome(n):
    a = str(n)
    b = ''.join(reversed(list(str(n))))
    return a == b


def buildList(n):
    gen_list1 = [['1']]
    gen_list2 = [['2']]
    while len(gen_list1) <= n:

        #starting with 1
        for digits in itertools.product(*gen_list1):
            digits_str = ''.join(digits)
            digits_rev = ''.join(reversed(digits))
            for i in ['', '0', '1', '2']:
                number = int(digits_str + i + digits_rev)
                if isPalindrome(number * number):
                    num_set2.add(number)
                    num_set.add(number * number)

        #starting with 2
        for digits in itertools.product(*gen_list2):
            digits_str = ''.join(digits)
            digits_rev = ''.join(reversed(digits))
            for i in ['', '0', '1', '2']:
                number = int(digits_str + i + digits_rev)
                if isPalindrome(number * number):
                    num_set2.add(number)
                    num_set.add(number * number)

        gen_list1 = gen_list1 + [['0', '1']]
        gen_list2 = gen_list2 + [['0']]


def solve(filename):

    buildList(25)
    raw_input("Press Enter to continue")

    fin = open(filename + '.in', 'r')
    fout = open(filename + '.out', 'w')

    T = int(fin.readline())
    for case in xrange(T):
        A, B = map(int, fin.readline().strip().split(' '))
        answer = len(filter(lambda x: A <= x <= B, num_set))
        print answer
        fout.write(('Case #%d: ' % (case + 1)) + str(answer) + '\n')

    fin.close()
    fout.close()


if __name__ == "__main__":
    # solve("C-tiny")
    # solve("C-small-attempt0")
    solve("C-large-1")
    # solve("C-large-2")