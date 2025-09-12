// JDBCExceptionDemo.java
import java.sql.*;

public class JDBCExceptionDemo {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/wrongdb"; // wrong DB to trigger error
        String user = "root";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            System.out.println("Connected!");
        } catch (SQLException e) {
            System.out.println("Database Error!");
            System.out.println("Error Code: " + e.getErrorCode());
            System.out.println("SQL State: " + e.getSQLState());
            System.out.println("Message: " + e.getMessage());
        }
    }
}
