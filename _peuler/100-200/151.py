def solve(A2, A3, A4, A5):
    k = tuple([A2, A3, A4, A5])
    if k == (0, 0, 0, 1):
        return 0
    elif k == (0, 0, 1, 0):
        return solve(0, 0, 0, 1) + 1
    elif k == (0, 1, 0, 0):
        return solve(0, 0, 1, 1) + 1
    elif k == (1, 0, 0, 0):
        return solve(0, 1, 1, 1) + 1
    else:
        pA2 = A2 * solve(A2 - 1, A3 + 1, A4 + 1, A5 + 1) if A2 > 0 else 0
        pA3 = A3 * solve(A2, A3 - 1, A4 + 1, A5 + 1) if A3 > 0 else 0
        pA4 = A4 * solve(A2, A3, A4 - 1, A5 + 1) if A4 > 0 else 0
        pA5 = A5 * solve(A2, A3, A4, A5 - 1) if A5 > 0 else 0
        return (pA2 + pA3 + pA4 + pA5) / float(A2 + A3 + A4 + A5)
        
print solve(1, 1, 1, 1)