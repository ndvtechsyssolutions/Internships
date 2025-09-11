import java.sql.*;
import java.util.Scanner;

public class ContactBookApp {
    static final String URL = "jdbc:mysql://localhost:3306/contact_book_db";
    static final String USER = "root"; // Replace if needed
    static final String PASS = "your_mysql_password"; // Replace with your MySQL password
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n1. Add Contact\n2. View Contacts\n3. Delete Contact\n0. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt(); sc.nextLine();
            switch (choice) {
                case 1 -> addContact();
                case 2 -> viewContacts();
                case 3 -> deleteContact();
                case 0 -> System.out.println("Goodbye!");
                default -> System.out.println("Invalid choice.");
            }
        } while (choice != 0);
    }

    static void addContact() {
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            System.out.print("Enter Name: ");
            String name = sc.nextLine();
            System.out.print("Enter Phone: ");
            String phone = sc.nextLine();
            System.out.print("Enter Email: ");
            String email = sc.nextLine();

            String sql = "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setString(1, name);
            ps.setString(2, phone);
            ps.setString(3, email);
            ps.executeUpdate();

            System.out.println("Contact added!");
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }

    static void viewContacts() {
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            String sql = "SELECT * FROM contacts";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            System.out.println("Contacts:");
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        ", Name: " + rs.getString("name") +
                        ", Phone: " + rs.getString("phone") +
                        ", Email: " + rs.getString("email"));
            }
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }

    static void deleteContact() {
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            System.out.print("Enter Contact ID to delete: ");
            int id = sc.nextInt(); sc.nextLine();
            String sql = "DELETE FROM contacts WHERE id = ?";
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setInt(1, id);
            int rows = ps.executeUpdate();
            if (rows > 0) System.out.println("Contact deleted!");
            else System.out.println("Contact not found.");
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
