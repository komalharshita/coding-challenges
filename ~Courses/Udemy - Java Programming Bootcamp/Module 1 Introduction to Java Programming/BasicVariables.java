import java.util.Scanner;

public class BasicVariables {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        System.out.print("Enter your GPA: ");
        double gpa = sc.nextDouble();

        System.out.println("My name is " + name + ", I am " + age + " years old, and my GPA is " + gpa);
    }
}
