package com.googlecodejam;

import java.io.*;
import java.util.*;

public class Main {

    public static int solve(int A, int B) {
        int result = 0;
        for (int n = A; n <= B; n++) {
            int numOfDigits = ((int) Math.log10(n)) + 1;
            if (numOfDigits == 1) continue;
            int temp = n;
            for (int i = 0; i < numOfDigits - 1; i++) {
                int remainder = temp % 10;
                if (remainder != 0) {
                    temp = (temp / 10) + remainder * ((int) Math.pow(10, numOfDigits - 1));
                    if (temp == n) break;
                    if ((temp > n) && (temp <= B)) {
                        result++;
                    }
                }
                else
                {
                    temp = (temp / 10) + remainder * ((int) Math.pow(10, numOfDigits - 1));
                }
            }
        }
        System.out.println(result);
        return result;
    }

    public static void main(String[] args) throws Exception {
        //String filename = "C-small-practice";
        String filename = "C-large-practice";
        String pwd = System.getProperty("user.dir");
        System.out.println(pwd);
        Scanner scanner = new Scanner(new FileReader(pwd + "\\" + filename + ".in"));
        PrintWriter printer = new PrintWriter(new FileWriter(pwd + "\\" + filename + ".out"));

        int caseCount = scanner.nextInt();
        for (int caseNumber = 1; caseNumber <= caseCount; caseNumber++) {
            printer.println("Case #" + caseNumber + ": " + solve(scanner.nextInt(), scanner.nextInt()));
        }

        printer.flush();
        printer.close();
        scanner.close();
    }
}
