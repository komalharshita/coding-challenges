// SimpleGUIDemo.java
import javax.swing.*;

public class SimpleGUIDemo {
    public static void main(String[] args) {
        // Create a JFrame (main window)
        JFrame frame = new JFrame("My First Swing App");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a label
        JLabel label = new JLabel("Hello, Java Swing!", SwingConstants.CENTER);

        // Add label to frame
        frame.add(label);

        // Make window visible
        frame.setVisible(true);
    }
}
