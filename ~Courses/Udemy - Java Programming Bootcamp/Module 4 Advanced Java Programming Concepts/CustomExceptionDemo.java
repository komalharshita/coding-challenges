// CustomExceptionDemo.java
import java.util.Scanner;

// Custom Exception
class AgeNotValidException extends Exception {
    AgeNotValidException(String msg) {
        super(msg);
    }
}

class Voter {
    void checkAge(int age) throws AgeNotValidException {
        if (age < 18) {
            throw new AgeNotValidException("Age must be 18 or above to vote.");
        } else {
            System.out.println("You are eligible to vote.");
        }
    }
}

public class CustomExceptionDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter age: ");
            int age = sc.nextInt();

            Voter v = new Voter();
            v.checkAge(age);

        } catch (AgeNotValidException e) {
            System.out.println("Custom Exception Caught: " + e.getMessage());
        } finally {
            System.out.println("Program finished.");
        }
    }
}
