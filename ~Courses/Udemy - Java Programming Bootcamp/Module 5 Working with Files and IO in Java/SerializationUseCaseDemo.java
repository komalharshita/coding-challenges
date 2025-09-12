// SerializationUseCaseDemo.java
import java.io.*;
import java.util.*;

class Employee implements Serializable {
    String name;
    String dept;
    double salary;

    Employee(String name, String dept, double salary) {
        this.name = name;
        this.dept = dept;
        this.salary = salary;
    }

    public String toString() {
        return name + " (" + dept + ") - $" + salary;
    }
}

public class SerializationUseCaseDemo {
    public static void main(String[] args) {
        List<Employee> employees = new ArrayList<>();
        employees.add(new Employee("Komal", "IT", 50000));
        employees.add(new Employee("Arjun", "HR", 45000));
        employees.add(new Employee("Neha", "Finance", 60000));

        // Serialize list of employees
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("employees.ser"))) {
            out.writeObject(employees);
            System.out.println("Employee list serialized!");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Deserialize list of employees
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream("employees.ser"))) {
            List<Employee> savedEmployees = (List<Employee>) in.readObject();
            System.out.println("\nDeserialized Employee List:");
            savedEmployees.forEach(System.out::println);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
