// VariablesDemo.java
import java.util.Scanner;

public class VariablesDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Declaration + initialization
        int a = 10;
        System.out.println("a = " + a);

        // 2. Multiple variables
        int x = 5, y = 15, z = 25;
        System.out.println("Sum of x,y,z = " + (x + y + z));

        // 3. Different data types
        String city = "Delhi";
        double temp = 32.5;
        System.out.println(city + " temperature: " + temp);

        // 4. User input
        System.out.print("Enter your name: ");
        String name = sc.nextLine();
        System.out.print("Enter your GPA: ");
        double gpa = sc.nextDouble();
        System.out.println(name + " has GPA " + gpa);

        // 5. Constants & scope
        final double PI = 3.14159;
        {
            int local = 50;
            System.out.println("PI = " + PI + ", local = " + local);
        }
    }
}
