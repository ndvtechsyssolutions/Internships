package jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class StudentCRUD {
    private static final String URL = "jdbc:mysql://localhost:3306/school";
    private static final String USER = "root";
    private static final String PASSWORD = "Yash@pandu";

    private static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    
    public static void createStudent(String name, int age) {
        String sql = "INSERT INTO Student (name, age) VALUES (?, ?)";
        try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.executeUpdate();
            System.out.println("Student created: " + name);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

  
    public static void readStudents() {
        String sql = "SELECT * FROM Student";
        try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
            ResultSet rs = pstmt.executeQuery();
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    
    public static void updateStudent(int id, String name, int age) {
        String sql = "UPDATE Student SET name = ?, age = ? WHERE id = ?";
        try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.setInt(3, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Student updated: ID = " + id);
            } else {
                System.out.println("No student found with ID = " + id);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    
    public static void deleteStudent(int id) {
        String sql = "DELETE FROM Student WHERE id = ?";
        try (Connection conn = getConnection(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Student deleted: ID = " + id);
            } else {
                System.out.println("No student found with ID = " + id);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        
        createStudent("Alice Brown", 19); 
        readStudents();                 
        updateStudent(1, "John Updated", 21); 
        readStudents();                 
        deleteStudent(2);               
        readStudents();                 
    }
}
