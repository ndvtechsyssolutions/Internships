package JDBC;

import java.sql.*;
import java.util.Scanner;

public class StudentCRUD {

    // Database connection details
    private static final String DB_URL = "jdbc:mysql://localhost:3306/testdb";
    static final String DB_USER = "root";
    static final String DB_PASS = "root@123";

    public static void main(String[] args) {
        // Try-with-resources ensures the connection is closed automatically
        try (Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS)) {
            Scanner input = new Scanner(System.in);
            int option;

            do {
                // Displaying menu options
                System.out.println("\n--- Student Management System ---");
                System.out.println("1. Add New Student");
                System.out.println("2. View All Students");
                System.out.println("3. Update Student Details");
                System.out.println("4. Delete Student Record");
                System.out.println("0. Exit");
                System.out.print("Enter your choice: ");
                option = input.nextInt();

                // Choosing operation based on user input
                switch (option) {
                    case 1 -> insertStudent(connection, input);
                    case 2 -> displayAllStudents(connection);
                    case 3 -> modifyStudent(connection, input);
                    case 4 -> removeStudent(connection, input);
                }
            } while (option != 0);

            System.out.println("Program Terminated.");

        } catch (SQLException e) {
            // Print SQL error if occurs
            e.printStackTrace();
        }
    }

    // Method to insert a new student record into the database
    private static void insertStudent(Connection connection, Scanner input) throws SQLException {
        System.out.print("Enter Student Name: ");
        input.nextLine();  // Clear buffer
        String studentName = input.nextLine();

        System.out.print("Enter Age: ");
        int studentAge = input.nextInt();

        System.out.print("Enter Grade: ");
        input.nextLine();  // Clear buffer again
        String studentGrade = input.nextLine();

        // SQL insert query
        String query = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, studentName);
            statement.setInt(2, studentAge);
            statement.setString(3, studentGrade);

            int result = statement.executeUpdate();
            System.out.println(result + " student added successfully.");
        }
    }

    // Method to view all student records
    private static void displayAllStudents(Connection connection) throws SQLException {
        String query = "SELECT * FROM students";

        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(query)) {

            System.out.println("\n--- List of Students ---");
            while (resultSet.next()) {
                System.out.printf("ID: %d | Name: %s | Age: %d | Grade: %s%n",
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getInt("age"),
                        resultSet.getString("grade"));
            }
        }
    }

    // Method to update an existing student record
    private static void modifyStudent(Connection connection, Scanner input) throws SQLException {
        System.out.print("Enter Student ID to update: ");
        int studentId = input.nextInt();

        System.out.print("Enter Updated Name: ");
        input.nextLine();  // Clear buffer
        String updatedName = input.nextLine();

        System.out.print("Enter Updated Age: ");
        int updatedAge = input.nextInt();

        System.out.print("Enter Updated Grade: ");
        input.nextLine();  // Clear buffer
        String updatedGrade = input.nextLine();

        String query = "UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, updatedName);
            statement.setInt(2, updatedAge);
            statement.setString(3, updatedGrade);
            statement.setInt(4, studentId);

            int result = statement.executeUpdate();
            System.out.println(result + " student record updated.");
        }
    }

    // Method to delete a student record by ID
    private static void removeStudent(Connection connection, Scanner input) throws SQLException {
        System.out.print("Enter Student ID to delete: ");
        int studentId = input.nextInt();

        String query = "DELETE FROM students WHERE id = ?";
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, studentId);

            int result = statement.executeUpdate();
            System.out.println(result + " student record deleted.");
        }
    }
}
