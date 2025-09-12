// JDBCCRUDDemo.java
import java.sql.*;

public class JDBCCRUDDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            Statement stmt = conn.createStatement();

            // Create table
            stmt.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age INT)");

            // Insert data
            stmt.executeUpdate("INSERT INTO students (name, age) VALUES ('Komal', 20), ('Arjun', 22)");

            // Read data
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            System.out.println("Student Records:");
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " - " + rs.getString("name") + " (" + rs.getInt("age") + ")");
            }

            // Update data
            stmt.executeUpdate("UPDATE students SET age = 21 WHERE name = 'Komal'");

            // Delete data
            stmt.executeUpdate("DELETE FROM students WHERE name = 'Arjun'");

            System.out.println("CRUD operations completed!");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
