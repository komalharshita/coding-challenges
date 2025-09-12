// FileReadWriteDemo.java
import java.io.*;
import java.util.Scanner;

public class FileReadWriteDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Writing to a file
        try (FileWriter fw = new FileWriter("sample.txt")) {
            System.out.print("Enter text to write into file: ");
            String text = sc.nextLine();
            fw.write(text);
            System.out.println("Data written to sample.txt");
        } catch (IOException e) {
            System.out.println("Error writing file: " + e.getMessage());
        }

        // Reading from the same file
        try (BufferedReader br = new BufferedReader(new FileReader("sample.txt"))) {
            String line;
            System.out.println("\nReading from file:");
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }
}

