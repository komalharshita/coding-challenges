// JDBCDemo.java
import java.sql.*;

public class JDBCDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/testdb"; // Change DB name
        String user = "root";  // your MySQL username
        String password = "password";  // your MySQL password

        try {
            // Load JDBC driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish connection
            Connection conn = DriverManager.getConnection(url, user, password);
            System.out.println("Connected to database successfully!");

            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
