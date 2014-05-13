pi = 3.14159265358979323846

T = int(raw_input().strip())

for case in xrange(T):
    N, F = map(int, raw_input().strip().split(' '))
    pies = map(int, raw_input().strip().split(' '))
    pies = map(lambda x: x*x*pi, pies)
    biggest = max(pies)
    left = 0
    right = biggest
    while left < right:
        mid = (right - left) / 2
        pie_count = sum(map(lambda x: x / mid, pies))
        print pie_count
        if pie_count < F + 1:
            right = mid
        elif pie_count > F + 1:
            left = mid
        else:
            print round(mid, 4)
            break