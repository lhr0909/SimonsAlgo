a = [i**2 for i in range(1,1002,2)]
b = [i**2 - 2*(i/2) for i in range(3,1002,2)]
c = [i**2 + 1 for i in range(2,1002,2)]
d = [(i**2 + 1) - 2*(i/2) for i in range(2,1002,2)]
print sum(a) + sum(b) + sum(c) + sum(d)