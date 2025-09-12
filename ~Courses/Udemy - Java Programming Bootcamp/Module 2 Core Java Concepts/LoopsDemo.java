// LoopsDemo.java
import java.util.Scanner;

public class LoopsDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. For loop - numbers 1 to 10
        for (int i = 1; i <= 10; i++) {
            System.out.print(i + " ");
        }
        System.out.println();

        // 2. While loop - sum of numbers
        System.out.print("Enter n: ");
        int n = sc.nextInt();
        int sum = 0, i = 1;
        while (i <= n) {
            sum += i;
            i++;
        }
        System.out.println("Sum = " + sum);

        // 3. Do-while - guessing
        int guess;
        do {
            System.out.print("Guess number (5 to exit): ");
            guess = sc.nextInt();
        } while (guess != 5);
        System.out.println("Correct! Exiting...");

        // 4. Multiplication table
        System.out.print("Enter number for table: ");
        int num = sc.nextInt();
        for (int j = 1; j <= 10; j++) {
            System.out.println(num + " x " + j + " = " + (num*j));
        }

        // 5. Nested loop pattern
        for (int row = 1; row <= 5; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
