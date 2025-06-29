package MYJDBC;

import java.sql.*;
import java.util.Scanner;

public class StudentCRUD {

    private static final String URL = "jdbc:mysql://localhost:3306/testdb";
    static final String USER = "root";
    static final String PASS = "DiVyA@1220"; 

    public static void main(String[] args) {
    	
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            Scanner scanner = new Scanner(System.in);
            int choice;

            do {
                System.out.println("\n--- Student Management ---");
                System.out.println("1. Add Student");
                System.out.println("2. View Students");
                System.out.println("3. Update Student");
                System.out.println("4. Delete Student");
                System.out.println("0. Exit");
                System.out.print("Enter choice: ");
                choice = scanner.nextInt();

                switch (choice) {
                    case 1 -> addStudent(conn, scanner);
                    case 2 -> viewStudents(conn);
                    case 3 -> updateStudent(conn, scanner);
                    case 4 -> deleteStudent(conn, scanner);
                }
            } while (choice != 0);

            System.out.println("Program Ended.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void addStudent(Connection conn, Scanner scanner) throws SQLException {
        System.out.print("Enter Name: ");
        scanner.nextLine();
        String name = scanner.nextLine();
        System.out.print("Enter Age: ");
        int age = scanner.nextInt();
        System.out.print("Enter Grade: ");
        scanner.nextLine();
        String grade = scanner.nextLine();

        String sql = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, name);
            stmt.setInt(2, age);
            stmt.setString(3, grade);
            int rows = stmt.executeUpdate();
            System.out.println(rows + " student added.");
        }
    }

    private static void viewStudents(Connection conn) throws SQLException {
        String sql = "SELECT * FROM students";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            System.out.println("\n--- Student Records ---");
            while (rs.next()) {
                System.out.printf("ID: %d | Name: %s | Age: %d | Grade: %s%n",
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getInt("age"),
                        rs.getString("grade"));
            }
        }
    }

    private static void updateStudent(Connection conn, Scanner scanner) throws SQLException {
        System.out.print("Enter Student ID to update: ");
        int id = scanner.nextInt();
        System.out.print("New Name: ");
        scanner.nextLine();
        String name = scanner.nextLine();
        System.out.print("New Age: ");
        int age = scanner.nextInt();
        System.out.print("New Grade: ");
        scanner.nextLine();
        String grade = scanner.nextLine();

        String sql = "UPDATE students SET name=?, age=?, grade=? WHERE id=?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, name);
            stmt.setInt(2, age);
            stmt.setString(3, grade);
            stmt.setInt(4, id);
            int rows = stmt.executeUpdate();
            System.out.println(rows + " record updated.");
        }
    }

    private static void deleteStudent(Connection conn, Scanner scanner) throws SQLException {
        System.out.print("Enter Student ID to delete: ");
        int id = scanner.nextInt();

        String sql = "DELETE FROM students WHERE id=?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, id);
            int rows = stmt.executeUpdate();
            System.out.println(rows + " record deleted.");
        }
    }
}
