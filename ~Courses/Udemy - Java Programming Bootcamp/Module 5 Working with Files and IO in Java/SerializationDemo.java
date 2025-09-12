// SerializationDemo.java
import java.io.*;

// Class must implement Serializable
class Student implements Serializable {
    String name;
    int age;
    double gpa;

    Student(String name, int age, double gpa) {
        this.name = name;
        this.age = age;
        this.gpa = gpa;
    }
}

public class SerializationDemo {
    public static void main(String[] args) {
        // Serialize object
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("student.ser"))) {
            Student s1 = new Student("Komal", 20, 8.9);
            out.writeObject(s1);
            System.out.println("Object serialized: " + s1.name);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Deserialize object
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("student.ser"))) {
            Student s2 = (Student) in.readObject();
            System.out.println("Object deserialized:");
            System.out.println("Name: " + s2.name + ", Age: " + s2.age + ", GPA: " + s2.gpa);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
