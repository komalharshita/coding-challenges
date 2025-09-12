// ClassUsageDemo.java
class Student {
    String name;
    int age;

    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class ClassUsageDemo {
    public static void main(String[] args) {
        // Creating and using objects
        Student s1 = new Student();
        s1.name = "Komal";
        s1.age = 19;
        s1.display();

        Student s2 = new Student();
        s2.name = "Arjun";
        s2.age = 20;
        s2.display();
    }
}
