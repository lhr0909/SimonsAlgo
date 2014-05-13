//pentagonal numbers are given by p(n) = n*(3*n-1)/2
//they are the partial sums of a(n) = 1+3*(n-1)
//test: if n = (sqrt(24*x+1)+1)/6 is a natural number, x is the n-th pentagonal number.

#include <stdio.h>
#include <math.h>

int testPentagonal(int n)
{
    if ((sqrt(24*n+1)+1) / 6 == (int) (sqrt(24*n+1)+1) / 6)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main(void)
{
    int flag = 0;
    int i = 1;
    int j;
    int diff;
    while (flag==0)
    {
        j = 1;
        while ((flag==0)&&(j<i))
        {
            diff = (i - j) * (3 * (i + j) - 1) / 2;
            if (testPentagonal(diff)==1)
            {
                if (testPentagonal((i * (3*i - 1) + j * (3*j - 1)) / 2)==1)
                {
                    printf("%d\n", diff);
                    flag = 1;
                }
            }
            j++;
        }
        i++;
    }
    return 0;
}

/*
Python Version:

from math import sqrt

testPentagonal = lambda n: True if (sqrt(24*n+1)+1) / 6 == int((sqrt(24*n+1)+1) / 6) else False

flag = True
i = 1
while flag:
    j = 1
    while flag and j<i:
        diff = (i - j) * (3 * (i + j) - 1) / 2
        if testPentagonal(diff):
            if testPentagonal((i * (3*i - 1) + j * (3*j - 1)) / 2):
                print diff
                flag = False
        j += 1
    i += 1
*/
