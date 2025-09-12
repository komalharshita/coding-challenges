// AbstractDemo.java
abstract class Vehicle {
    abstract void start();
    void fuel() { System.out.println("Filling fuel..."); }
}

class Bike extends Vehicle {
    void start() { System.out.println("Bike starts with a kick"); }
}

class Car extends Vehicle {
    void start() { System.out.println("Car starts with a key"); }
}

public class AbstractDemo {
    public static void main(String[] args) {
        Vehicle v1 = new Bike();
        v1.start();
        v1.fuel();

        Vehicle v2 = new Car();
        v2.start();
        v2.fuel();
    }
}
