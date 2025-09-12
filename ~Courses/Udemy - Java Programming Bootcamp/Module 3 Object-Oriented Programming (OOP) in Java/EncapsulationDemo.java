// EncapsulationDemo.java
class Employee {
    private String name;
    private double salary;

    // Getter and Setter
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public double getSalary() { return salary; }
    public void setSalary(double salary) {
        if (salary >= 0) this.salary = salary;
        else System.out.println("Invalid salary!");
    }
}

public class EncapsulationDemo {
    public static void main(String[] args) {
        Employee e = new Employee();
        e.setName("Komal");
        e.setSalary(50000);

        System.out.println("Employee: " + e.getName());
        System.out.println("Salary: " + e.getSalary());
    }
}
