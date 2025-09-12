// EventHandlingDemo.java
import javax.swing.*;
import java.awt.event.*;

public class EventHandlingDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Event Handling Example");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Button
        JButton button = new JButton("Click Me!");
        JLabel label = new JLabel("Waiting for click...", SwingConstants.CENTER);

        // Event handling using ActionListener
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                label.setText("Button was clicked!");
            }
        });

        frame.setLayout(new java.awt.BorderLayout());
        frame.add(button, java.awt.BorderLayout.SOUTH);
        frame.add(label, java.awt.BorderLayout.CENTER);

        frame.setVisible(true);
    }
}
