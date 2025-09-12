// ClassObjectDemo.java
class Car {
    String brand;
    int speed;

    void drive() {
        System.out.println(brand + " is driving at " + speed + " km/h");
    }
}

public class ClassObjectDemo {
    public static void main(String[] args) {
        // Creating objects
        Car car1 = new Car();
        car1.brand = "Honda";
        car1.speed = 80;

        Car car2 = new Car();
        car2.brand = "Tesla";
        car2.speed = 120;

        // Using objects
        car1.drive();
        car2.drive();
    }
}
