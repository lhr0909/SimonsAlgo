numerator = [3, 7] + [0] * 998
denominator = [2, 5] + [0] * 998
count = 0
for i in range(2, 1000):
    numerator[i] = 2 * numerator[i-1] + numerator[i-2]
    denominator[i] = denominator[i-1] + numerator[i-1]
    if len(str(numerator[i])) > len(str(denominator[i])):
        count += 1

print count

