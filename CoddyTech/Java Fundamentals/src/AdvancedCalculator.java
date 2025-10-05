import java.util.Scanner;

public class AdvancedCalculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {

            String input = sc.nextLine();

            if (input.charAt(0) == 'e') {
                break; // Exit the loop if the user enters 'e'
            }

            char operation = input.charAt(0);
            float n1 = sc.nextFloat();
            float n2 = sc.nextFloat();
            sc.nextLine(); // Consume the newline character

            float res = 0;
            boolean validOperation = true;

            switch (operation) {
                case '+':
                    res = n1 + n2;
                    break;
                case '-':
                    res = n1 - n2;
                    break;
                case '*':
                    res = n1 * n2;
                    break;
                case '/':
                    if (n2 != 0) {
                        res = n1 / n2;
                    } else {

                        validOperation = false;
                    }
                    break;
                default:
                    validOperation = false;
            }

            if (validOperation) {
                System.out.println(res);
            }
        }

        sc.close(); // Close the scanner to prevent resource leaks
    }
}
