// ConditionalsDemo.java
import java.util.Scanner;

public class ConditionalsDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Positive or Negative
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        if (num >= 0) System.out.println("Positive");
        else System.out.println("Negative");

        // 2. Largest of two
        System.out.print("Enter two numbers: ");
        int a = sc.nextInt(), b = sc.nextInt();
        System.out.println("Larger is: " + (a>b ? a : b));

        // 3. Grading system
        System.out.print("Enter marks: ");
        int marks = sc.nextInt();
        if (marks >= 90) System.out.println("Grade A");
        else if (marks >= 75) System.out.println("Grade B");
        else if (marks >= 50) System.out.println("Grade C");
        else System.out.println("Fail");

        // 4. Switch for days
        System.out.print("Enter day number (1-7): ");
        int day = sc.nextInt();
        switch(day) {
            case 1 -> System.out.println("Monday");
            case 2 -> System.out.println("Tuesday");
            case 3 -> System.out.println("Wednesday");
            case 4 -> System.out.println("Thursday");
            case 5 -> System.out.println("Friday");
            case 6 -> System.out.println("Saturday");
            case 7 -> System.out.println("Sunday");
            default -> System.out.println("Invalid");
        }

        // 5. Nested If
        System.out.print("Enter age: ");
        int age = sc.nextInt();
        if (age >= 18) {
            if (age >= 60) System.out.println("Senior Citizen");
            else System.out.println("Adult");
        } else System.out.println("Minor");
    }
}

