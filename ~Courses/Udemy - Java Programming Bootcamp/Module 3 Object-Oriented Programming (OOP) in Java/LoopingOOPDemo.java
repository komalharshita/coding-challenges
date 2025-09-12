// LoopingOOPDemo.java
import java.util.Scanner;

class LoopingHelper {
    // Method to print multiplication table
    void printTable(int n) {
        for (int i = 1; i <= 10; i++) {
            System.out.println(n + " x " + i + " = " + (n*i));
        }
    }

    // Method to calculate sum using while loop
    int sumNumbers(int n) {
        int sum = 0, i = 1;
        while (i <= n) {
            sum += i;
            i++;
        }
        return sum;
    }

    // Method to use do-while for password check
    void passwordCheck() {
        Scanner sc = new Scanner(System.in);
        String password;
        do {
            System.out.print("Enter password (hint: java123): ");
            password = sc.nextLine();
        } while (!password.equals("java123"));
        System.out.println("Access granted!");
    }
}

public class LoopingOOPDemo {
    public static void main(String[] args) {
        LoopingHelper helper = new LoopingHelper();
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a number for table: ");
        int num = sc.nextInt();
        helper.printTable(num);

        System.out.print("Enter n for sum: ");
        int n = sc.nextInt();
        System.out.println("Sum = " + helper.sumNumbers(n));

        helper.passwordCheck();
    }
}
