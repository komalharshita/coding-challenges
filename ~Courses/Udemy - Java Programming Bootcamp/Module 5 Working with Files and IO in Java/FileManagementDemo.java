// FileManagementDemo.java
import java.io.File;
import java.io.IOException;

public class FileManagementDemo {
    public static void main(String[] args) {
        try {
            File file = new File("data.txt");

            // Create new file
            if (file.createNewFile()) {
                System.out.println("File created: " + file.getName());
            } else {
                System.out.println("File already exists.");
            }

            // File info
            System.out.println("Absolute Path: " + file.getAbsolutePath());
            System.out.println("Writable: " + file.canWrite());
            System.out.println("Readable: " + file.canRead());
            System.out.println("File size: " + file.length() + " bytes");

            // Delete file
            if (file.delete()) {
                System.out.println("File deleted successfully.");
            } else {
                System.out.println("Failed to delete file.");
            }

        } catch (IOException e) {
            System.out.println("An error occurred.");
        }
    }
}
