import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int arraySize;
        String firstElement;
        List<String> numbers = Arrays.asList("0", "1", "2", "3", "5", "6", "7", "8", "9");
        Integer[] integerArray;
        String[] stringArray;
        
        while(scanner.hasNext()) {
            arraySize = Integer.parseInt(scanner.nextLine());
            
            firstElement = scanner.nextLine();
            if (numbers.contains(firstElement)) {
                integerArray = new Integer[arraySize];
                integerArray[0] = Integer.parseInt(firstElement);
                
                for (int i = 1; i < arraySize; i++) {
                    integerArray[i] = Integer.parseInt(scanner.nextLine());
                }
                
                printArray(integerArray);
            } else {
                stringArray = new String[arraySize];
                stringArray[0] = firstElement;
                
                for (int i = 1; i < arraySize; i++) {
                    stringArray[i] = scanner.nextLine();
                }
                                
                printArray(stringArray);
            }
        }
        
        scanner.close();
    }
    
    private static <E> void printArray(E[] a) {
        for (E e: a) {
            System.out.println(e);            
        }
    }
}
