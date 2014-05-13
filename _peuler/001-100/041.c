#include <stdio.h>
#include <math.h>

/*
*Apparently*, it cannot be 9-digit or 8-digit pandigital, because the digits add up to 45 or 36, which is divisible by 9.
Should be in the 7-digit pandigital numbers. find the total permutation, check isPrime() on every one.
Article on total permutation: http://www.cut-the-knot.org/do_you_know/AllPerm.shtml
Related to Project Euler 024 (for finding permutations).

Quoted from the forum thread:
"First I used reasoning.
We know that the max value is at least 4231.
It can't be 5 digits, because 1+2+3+4+5 = 15 which means that any permutation of the digits will result in a multiple of 3.
adding a 6 won't help either: 3 divides 21 as well. 
7 is fine (1+2+3+4+5+6+7=28).
8 digits doesn't work, because 1+2+3+4+5+6+7+8 = 36 which is divible by 3.
Similarly, 9 digits won't work because the sum of the digits is 45 => a multiple of 3. 
Therefore, the max prime is going to be either 7 digits long or 4 digits long."
*/

int isPrime(long n)
{
    long i;
    if (n < 2)
    {
        return 0;
    }
    for (i = 2; i <= (int) sqrt(n); i++)
    {
        if (n % i==0)
        {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    int digit[7] = {1, 2, 3, 4, 5, 6, 7};
    int a;
    int totalPermutation = 7*6*5*4*3*2;
    int temp;
    int k = 7;
    int number;
    int max = 0;
    for (a = 0; a < totalPermutation; a++)
    {
        int i = k - 1;

        while (digit[i-1] >= digit[i]) i--;

        int j = k;

        while (digit[j-1] <= digit[i-1]) j--;
        temp = digit[i-1];
        digit[i-1] = digit[j-1];
        digit[j-1] = temp;

        i++;
        j = k;

        while (i < j)
        {
            temp = digit[i-1];
            digit[i-1] = digit[j-1];
            digit[j-1] = temp;
            i++;
            j--;
        }
        number = digit[0] * 1000000 + digit[1] * 100000 + digit[2] * 10000 + digit[3] * 1000 + digit[4] * 100 + digit[5] * 10 + digit[6];
        if (isPrime(number)==1)
        {
            if (number>max)
            {
                max = number;
            }
        }
    }
    printf("%d\n", max);
    return 0;
}
