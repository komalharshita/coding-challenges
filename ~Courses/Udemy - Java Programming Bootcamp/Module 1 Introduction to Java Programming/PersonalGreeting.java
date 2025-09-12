import java.util.Scanner;

public class PersonalGreeting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        sc.nextLine(); // clear buffer
        System.out.print("Enter your favorite hobby: ");
        String hobby = sc.nextLine();

        System.out.println("My name is " + name + ", I am " + age + " years old, and I love " + hobby + ".");
    }
}
