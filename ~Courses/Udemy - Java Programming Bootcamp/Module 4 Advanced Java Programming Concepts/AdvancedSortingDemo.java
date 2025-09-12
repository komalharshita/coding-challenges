// AdvancedSortingDemo.java
import java.util.*;

class Student {
    String name;
    int age;
    double gpa;

    Student(String name, int age, double gpa) {
        this.name = name;
        this.age = age;
        this.gpa = gpa;
    }

    public String toString() {
        return name + " (Age: " + age + ", GPA: " + gpa + ")";
    }
}

public class AdvancedSortingDemo {
    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        students.add(new Student("Komal", 20, 8.9));
        students.add(new Student("Arjun", 22, 7.5));
        students.add(new Student("Neha", 21, 9.1));

        // Sort by age (Ascending)
        students.sort(Comparator.comparingInt(s -> s.age));
        System.out.println("Sorted by Age: " + students);

        // Sort by GPA (Descending)
        students.sort((s1, s2) -> Double.compare(s2.gpa, s1.gpa));
        System.out.println("Sorted by GPA: " + students);

        // Sort by Name (Alphabetical)
        students.sort(Comparator.comparing(s -> s.name));
        System.out.println("Sorted by Name: " + students);
    }
}
