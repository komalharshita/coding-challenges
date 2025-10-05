import java.util.Scanner;

public class GuesstheNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int randNum = scanner.nextInt(); // Input for random number
        int guess = scanner.nextInt();    // Input for user's guess

        if (guess > randNum) {
            System.out.println("Too high");
        }
        if (guess < randNum) {
            System.out.println("Too low");
        }
        if (guess == randNum) { // Use '==' for comparison
            System.out.println("You are right!");
        }
        // Write code here
    }
}
