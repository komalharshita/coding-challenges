// ThreadCreationDemo.java
class RunnableTask implements Runnable {
    private String taskName;

    RunnableTask(String name) {
        this.taskName = name;
    }

    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println(taskName + " is running - step " + i);
            try { Thread.sleep(300); } catch (InterruptedException e) {}
        }
    }
}

public class ThreadCreationDemo {
    public static void main(String[] args) {
        // Thread using Runnable
        Thread t1 = new Thread(new RunnableTask("Task A"));
        Thread t2 = new Thread(new RunnableTask("Task B"));

        // Starting threads
        t1.start();
        t2.start();

        // Managing threads (join ensures main waits)
        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {}

        System.out.println("Both tasks completed!");
    }
}
