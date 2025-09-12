// LayoutManagerDemo.java
import javax.swing.*;
import java.awt.*;

public class LayoutManagerDemo {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Layout Manager Example");
        frame.setSize(500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Using BorderLayout
        frame.setLayout(new BorderLayout());

        // Panels with different layouts
        JPanel topPanel = new JPanel(new FlowLayout());
        topPanel.add(new JButton("Button 1"));
        topPanel.add(new JButton("Button 2"));

        JPanel centerPanel = new JPanel(new GridLayout(2, 2));
        centerPanel.add(new JButton("A"));
        centerPanel.add(new JButton("B"));
        centerPanel.add(new JButton("C"));
        centerPanel.add(new JButton("D"));

        JPanel bottomPanel = new JPanel();
        bottomPanel.add(new JLabel("Status: Ready"));

        // Adding panels to frame
        frame.add(topPanel, BorderLayout.NORTH);
        frame.add(centerPanel, BorderLayout.CENTER);
        frame.add(bottomPanel, BorderLayout.SOUTH);

        frame.setVisible(true);
    }
}
