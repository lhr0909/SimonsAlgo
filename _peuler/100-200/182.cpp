#include <iostream>
using namespace std;

//http://en.wikipedia.org/wiki/Modular_exponentiation
//http://books.google.com/books?id=nSzoG72E93MC&pg=PA290&lpg=PA290&dq=RSA+number+of+unconcealed+message&source=bl&ots=MuFiCcpKdL&sig=ZuR3mFrRHZMe9Ipb8kzHbENej_g&hl=en&ei=-ioaTLLPKc6TkAWXsPGvBg&sa=X&oi=book_result&ct=result&resnum=4&ved=0CC4Q6AEwAw#v=onepage&q=RSA%20number%20of%20unconcealed%20message&f=false
//http://www.security-forums.com/viewtopic.php?t=29782&sid=59d66fe2ba8ae0fd775442f55a03d683

//number of unconcealed message is given by
//(1 + gcd(e-1, p-1)) * (1 + gcd(e-1, q-1))
//and the number of unconcealed message is at least 9.

//Proof:
//p-1 is even. If e is even, 
//then e has a common factor with phi(n)=(p-1)*(q-1). 
//So e has to be odd such that e*d==1 mod phi (n). Therefore e-1 is even. 
//Since p-1 and e-1 are even, their gcd is at least two and 
//(gcd(e-1, p-1) + 1) = at least 3 and 
//(gcd(e-1, q-1) + 1)= at least 3. 
//Hence their product is at least 9. 

long gcd(long a, long b)
{
    long t;
    while (b != 0)
    {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}

/*
long powmod(long base, long exp, long mod)
{
    long result = 1;
 
    while (exp > 0) {
        if (exp & 1) {
            // multiply in this bit's contribution while using modulus to keep result small
            result = (result * base) % mod;
        }
        // move to the next bit of the exponent, square (and mod) the base accordingly
        exp >>= 1;
        base = (base * base) % mod;
    }
 
    return result;
}
*/

//uses the formula, and runs in about 1 sec with my Athlon 64 X2 4200+ (2.20GHz)
int main()
{
    //long p = 19;
    //long q = 37;
    long p = 1009;
    long q = 3643;
    long n = p * q;
    long p_1 = p - 1;
    long q_1 = q - 1;
    long phi = p_1 * q_1;
    long long sum = 0; //not big enough the first time...
    
    //cout << n << " " << phi << endl;
    
    for (long e = 2; e < phi; e++)
    {
        if (gcd(e, phi) == 1)
        {
            long k = e - 1;
            long long count = (1 + gcd(k, p_1)) * (1 + gcd(k, q_1));
            if (count == 9)
            {
                sum += e;
                //cout << e << " " << sum << endl;
            }
        }
    }
    cout << sum << endl;
    //system("pause");
    return 0;
}
