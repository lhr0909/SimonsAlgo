'''
http://www.maztravel.com/haskell/euler_problem_191.html

for a length of 3, we have these options:
OOO
OOA
OOL
OAO
OAA
OAL
OLO
OLA
OLL -- X
AOO
AOA
AOL
AAO
AAA -- X
AAL
ALO
ALA
ALL -- X
LOO
LOA
LOL -- X
LAO
LAA
LAL -- X
LLO -- X
LLA -- X
LLL -- X

and then, we basically just categorize it into different subgroups

prize(n) is the number of prize strings of length n which are valid in the problem
NotTwoAs(n) is the number of prize strings of length n which don't end with two A's
NoLs(n) is the number of prize strings of length n which don't contain any L's
NotOneA(n) is the number of prize strings of length n which don't end with one A
NoLsANDTwoAs(n) is the number of prize strings of length n which don't end with two A's
    and don't have any L's
NoLsANDOneA(n) is the number of prize strings of length n which don't end with one A
    and don't have any L's

So prize(3) = 19
and when n > 3, prize(n) = prize(n - 1) + NotTwoAs(n - 1) + NoLs(n - 1)
                             (add O)          (add A)          (add L)

NotTwoAs(3) = 17
and when n > 3, NotTwoAs(n) = prize(n - 1) + NotOneA(n - 1) + NoLs(n - 1)
                               (add O)          (add A)          (add L)

NotOneA(3) = 12
and when n > 3, NotOneA(n) = prize(n - 1) + NoLs(n - 1)
                              (add O)         (add L)
No A's added for NotOneA because no A's are allowed in the end

NoLs(3) = 7
and when n > 3, NoLs(n) = NoLs(n - 1) + NoLsANDTwoAs(n - 1)
                            (add O)        (add A)

NoLsANDTwoAs(3) = 6
and when n > 3, NoLsANDTwoAs(n) = NoLs(n - 1) + NoLsANDOneA(n - 1)
                                   (add O)         (add A)

NoLsANDOneA(3) = 4
and when n > 3, NoLsANDOneA(n) = NoLs(n - 1)
                                   (add O)
'''

prize = dict()
NotTwoAs = dict()
NotOneA = dict()
NoLs = dict()
NoLsANDTwoAs = dict()
NoLsANDOneA = dict()

prize[3] = 19
NotTwoAs[3] = 17
NotOneA[3] = 12
NoLs[3] = 7
NoLsANDTwoAs[3] = 6
NoLsANDOneA[3] = 4

for i in xrange(4, 31):
    prize[i] = prize[i - 1] + NotTwoAs[i - 1] + NoLs[i - 1]
    NotTwoAs[i] = prize[i - 1] + NotOneA[i - 1] + NoLs[i - 1]
    NotOneA[i] = prize[i - 1] + NoLs[i - 1]
    NoLs[i] = NoLs[i - 1] + NoLsANDTwoAs[i - 1]
    NoLsANDTwoAs[i] = NoLs[i - 1] + NoLsANDOneA[i - 1]
    NoLsANDOneA[i] = NoLs[i - 1]

print prize[30]

'''
I derived the direct recursive formula:
  t(n) = 2*t(n-1)+t(n-2)-3*t(n-4)-2*t(n-5)-t(n-6)

Together with the initial conditions:
  t(0)=1; t(1)=3; t(2)=8;
  t(3)=19; t(4)=43; t(5)=94;
'''