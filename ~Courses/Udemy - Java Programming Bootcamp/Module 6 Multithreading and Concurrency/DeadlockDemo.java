// DeadlockDemo.java
class Resource {
    String name;
    Resource(String name) { this.name = name; }
}

public class DeadlockDemo {
    public static void main(String[] args) {
        Resource r1 = new Resource("Resource1");
        Resource r2 = new Resource("Resource2");

        // Thread 1 locks r1 then tries to lock r2
        Thread t1 = new Thread(() -> {
            synchronized (r1) {
                System.out.println("Thread-1 locked " + r1.name);
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (r2) {
                    System.out.println("Thread-1 locked " + r2.name);
                }
            }
        });

        // Thread 2 locks r2 then tries to lock r1
        Thread t2 = new Thread(() -> {
            synchronized (r2) {
                System.out.println("Thread-2 locked " + r2.name);
                try { Thread.sleep(100); } catch (InterruptedException e) {}
                synchronized (r1) {
                    System.out.println("Thread-2 locked " + r1.name);
                }
            }
        });

        t1.start();
        t2.start();
    }
}
