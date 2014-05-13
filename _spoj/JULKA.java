package spoj;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s;
        BigInteger x, y, m, n;
        for (int tests = 0; tests < 10; tests++) {
            s = in.nextLine();
            n = new BigInteger(s);
            s = in.nextLine();
            m = new BigInteger(s);
            x = (n.add(m)).divide(BigInteger.valueOf(2));
            y = (n.subtract(m)).divide(BigInteger.valueOf(2));
            System.out.println(x);
            if (tests == 9)
                System.out.print(y);
            else
                System.out.println(y);
        }
    }
}
