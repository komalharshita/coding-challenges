// CollectionAlgorithmsDemo.java
import java.util.*;

public class CollectionAlgorithmsDemo {
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>(Arrays.asList(5, 2, 8, 1, 3));

        // Sorting
        Collections.sort(nums);
        System.out.println("Sorted List: " + nums);

        // Searching
        int index = Collections.binarySearch(nums, 3);
        System.out.println("Element 3 found at index: " + index);

        // Iterating with for-each
        System.out.print("For-each loop: ");
        for (int n : nums) {
            System.out.print(n + " ");
        }

        // Iterating with Iterator
        System.out.print("\nUsing Iterator: ");
        Iterator<Integer> it = nums.iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
    }
}
