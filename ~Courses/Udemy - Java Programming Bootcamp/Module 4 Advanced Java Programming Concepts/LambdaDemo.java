// LambdaDemo.java
import java.util.*;

interface MathOperation {
    int operate(int a, int b);
}

public class LambdaDemo {
    public static void main(String[] args) {
        // Lambda for addition
        MathOperation add = (a, b) -> a + b;
        System.out.println("Addition: " + add.operate(5, 3));

        // Lambda for multiplication
        MathOperation mul = (a, b) -> a * b;
        System.out.println("Multiplication: " + mul.operate(5, 3));

        // Lambda with forEach
        List<String> names = Arrays.asList("Komal", "Arjun", "Neha");
        System.out.println("Names:");
        names.forEach(n -> System.out.println("Hello " + n));

        // Lambda with Comparator
        List<Integer> nums = Arrays.asList(5, 2, 8, 1, 3);
        nums.sort((x, y) -> y - x); // Descending order
        System.out.println("Sorted Descending: " + nums);
    }
}
