#Solving Pell's Equation

#The series is the generating function for the fibonacci sequence, which is
#f(x) = x / (1 - x - x^2)

#Solve f(x) = k for x in Maple, we have
#x = (sqrt(1 + 2*k + 5*k^2) - 1 - k) / (2 * k) or
#x = (sqrt(1 + 2*k + 5*k^2) + 1 + k) / (-2 * k)

#Since x needs to be rational, which means
#1 + 2*k + 5*k^2 has to be a perfect square

#1 + 2*k + 5*k^2 = r^2
#multiply both sides by 5
#5 + 10*k + 25*k^2 = 5*r^2
#(5*k + 1)^2 + 4 = 5*r^2
#(5*k + 1)^2 - 5*r^2 = -4

#So let
#A = 5*k + 1
#B = r
#We are essentially solving the Pell's Equation
#A^2 - 5*B^2 = -4
#where A % 5 = 1

#And as you can see, the fundamental solution should be A = 1, B = 1

#this time I will try to use a new method to calculate the equation

#http://en.wikipedia.org/wiki/Pell%27s_equation
#('additional solutions from the fundamental solution')

#http://d.hatena.ne.jp/inamori/20091231/p1

x1 = 1
y1 = 1

xk_1 = x1
yk_1 = y1

count = 0
while count < 15:
    xk = (x1 * xk_1 + 5 * y1 * yk_1) / 2
    yk = (x1 * yk_1 + y1 * xk_1) / 2
    if xk % 5 == 1:
        #print (xk - 1) / 5
        count += 1
    xk_1 = xk
    yk_1 = yk
print (xk - 1) / 5