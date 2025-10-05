import java.util.Scanner;

public class decisionmaking {
    public static void main(String[] args) {
        int a = 9;
        int b = 9;

        // Don't change below this line
        if (a >= b) {
            System.out.println("You are here!");
        }

        Scanner scanner = new Scanner(System.in);
        int age = scanner.nextInt();
        // Don't touch above this line
        // Write code here
        if (age > 18) {
            System.out.println("Above 18");
        }
        if (age <= 18) {
            System.out.println("Below or equal 18");
        }
    }
}
