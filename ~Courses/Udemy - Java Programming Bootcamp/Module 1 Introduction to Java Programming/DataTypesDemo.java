// DataTypesDemo.java
import java.util.Scanner;

public class DataTypesDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // 1. Primitive types
        int age = 20;
        double height = 5.8;
        char grade = 'A';
        boolean student = true;
        System.out.println("Age: " + age + ", Height: " + height + ", Grade: " + grade + ", Student? " + student);

        // 2. Input primitive
        System.out.print("Enter an integer: ");
        int num = sc.nextInt();
        System.out.print("Enter a decimal: ");
        double dec = sc.nextDouble();
        System.out.println("You entered int=" + num + " and double=" + dec);

        // 3. Type casting
        double d = 9.99;
        int casted = (int) d;
        System.out.println("Original double: " + d + " → After cast: " + casted);

        // 4. String methods
        String name = "Komal";
        System.out.println("Upper: " + name.toUpperCase() + ", Length: " + name.length());

        // 5. Wrapper class
        Integer x = num;
        Double y = dec;
        System.out.println("Wrapper Integer: " + x + ", Wrapper Double: " + y);
    }
}
