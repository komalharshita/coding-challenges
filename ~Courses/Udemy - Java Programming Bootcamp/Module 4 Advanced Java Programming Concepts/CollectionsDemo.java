// CollectionsDemo.java
import java.util.*;

public class CollectionsDemo {
    public static void main(String[] args) {
        // List
        List<String> fruits = new ArrayList<>();
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Mango");
        System.out.println("List: " + fruits);

        // Set
        Set<Integer> numbers = new HashSet<>();
        numbers.add(10);
        numbers.add(20);
        numbers.add(10); // duplicate ignored
        System.out.println("Set: " + numbers);

        // Map
        Map<Integer, String> students = new HashMap<>();
        students.put(1, "Komal");
        students.put(2, "Arjun");
        students.put(3, "Neha");
        System.out.println("Map: " + students);

        // Queue
        Queue<String> queue = new LinkedList<>();
        queue.add("Task1");
        queue.add("Task2");
        queue.add("Task3");
        System.out.println("Queue: " + queue);
        System.out.println("Polling Queue: " + queue.poll());
        System.out.println("Queue after poll: " + queue);
    }
}
