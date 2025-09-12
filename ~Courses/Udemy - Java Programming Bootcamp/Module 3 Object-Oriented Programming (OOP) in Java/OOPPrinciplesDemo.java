// OOPPrinciplesDemo.java

// Encapsulation
class BankAccount {
    private double balance;

    public void deposit(double amount) { balance += amount; }
    public void withdraw(double amount) {
        if (balance >= amount) balance -= amount;
        else System.out.println("Insufficient funds");
    }
    public double getBalance() { return balance; }
}

// Inheritance
class Animal {
    void sound() { System.out.println("Animal makes a sound"); }
}

class Dog extends Animal {
    void sound() { System.out.println("Dog barks"); } // Polymorphism (overriding)
}

// Abstraction
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    void draw() { System.out.println("Drawing Circle"); }
}

public class OOPPrinciplesDemo {
    public static void main(String[] args) {
        // Encapsulation
        BankAccount acc = new BankAccount();
        acc.deposit(1000);
        acc.withdraw(300);
        System.out.println("Balance: " + acc.getBalance());

        // Inheritance + Polymorphism
        Animal a = new Dog();
        a.sound();

        // Abstraction
        Shape s = new Circle();
        s.draw();
    }
}
