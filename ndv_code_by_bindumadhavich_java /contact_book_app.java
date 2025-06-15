# SQL code for connected to java 

CREATE DATABASE contact_book;
USE contact_book;
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255)
);

#java program for sql connecter

package contact_book_app;

import java.sql.*;
import java.util.*;
import java.io.*;

public class ContactBookApp {
    static final String DB_URL = "jdbc:mysql://localhost:3306/contact_book";
    static final String USER = "root";
    static final String PASS = "system"; // ← change this
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        while (true) {
            System.out.println("\n===== Contact Book Menu =====");
            System.out.println("1. Add Contact");
            System.out.println("2. View All Contacts");
            System.out.println("3. Update Contact");
            System.out.println("4. Delete Contact");
            System.out.println("5. Search Contact");
            System.out.println("6. Sort Contacts by Name");
            System.out.println("7. Export to CSV");
            System.out.println("8. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt(); sc.nextLine();
            switch (choice) {
                case 1: addContact(); break;
                case 2: viewContacts(); break;
                case 3: updateContact(); break;
                case 4: deleteContact(); break;
                case 5: searchContact(); break;
                case 6: sortContacts(); break;
                case 7: exportToCSV(); break;
                case 8: System.out.println("Goodbye!"); System.exit(0);
                default: System.out.println("Invalid choice!");
            }
        }
    }
    static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(DB_URL, USER, PASS);
    }
    static void addContact() {
        try (Connection conn = getConnection()) {
            System.out.print("Enter name: ");
            String name = sc.nextLine();
            System.out.print("Enter phone number: ");
            String phone = sc.nextLine();
            System.out.print("Enter email: ");
            String email = sc.nextLine();
            System.out.print("Enter address: ");
            String address = sc.nextLine();
            if (!phone.matches("\\d{10}")) {
                System.out.println("Invalid phone number!");
                return;
            }
            if (!email.matches("^[\\w.-]+@[\\w.-]+\\.[a-zA-Z]{2,}$")) {
                System.out.println("Invalid email format!");
                return;
            }
            String sql = "INSERT INTO contacts (name, phone_number, email, address) VALUES (?, ?, ?, ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, name);
            stmt.setString(2, phone);
            stmt.setString(3, email);
            stmt.setString(4, address);
            stmt.executeUpdate();
            System.out.println("Contact added successfully.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    static void viewContacts() {
        try (Connection conn = getConnection()) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM contacts");
            System.out.println("\nContacts List:");
            while (rs.next()) {
                System.out.printf("ID: %d | Name: %s | Phone: %s | Email: %s | Address: %s\n",
                        rs.getInt("id"), rs.getString("name"), rs.getString("phone_number"),
                        rs.getString("email"), rs.getString("address"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    static void updateContact() {
        try (Connection conn = getConnection()) {
            System.out.print("Enter contact ID to update: ");
            int id = sc.nextInt(); sc.nextLine();
            System.out.print("New name: ");
            String name = sc.nextLine();
            System.out.print("New phone: ");
            String phone = sc.nextLine();
            System.out.print("New email: ");
            String email = sc.nextLine();
            System.out.print("New address: ");
            String address = sc.nextLine();
            String sql = "UPDATE contacts SET name=?, phone_number=?, email=?, address=? WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, name);
            stmt.setString(2, phone);
            stmt.setString(3, email);
            stmt.setString(4, address);
            stmt.setInt(5, id);
            int rows = stmt.executeUpdate();
            System.out.println(rows > 0 ? "Contact updated." : "Contact not found.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    static void deleteContact() {
        try (Connection conn = getConnection()) {
            System.out.print("Enter contact ID to delete: ");
            int id = sc.nextInt(); sc.nextLine();
            String sql = "DELETE FROM contacts WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);
            int rows = stmt.executeUpdate();
            System.out.println(rows > 0 ? "Contact deleted." : "Contact not found.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    static void searchContact() {
        try (Connection conn = getConnection()) {
            System.out.print("Search by name or phone: ");
            String keyword = sc.nextLine();
            String sql = "SELECT * FROM contacts WHERE name LIKE ? OR phone_number LIKE ?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, "%" + keyword + "%");
            stmt.setString(2, "%" + keyword + "%");
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                System.out.printf("ID: %d | Name: %s | Phone: %s | Email: %s | Address: %s\n",
                        rs.getInt("id"), rs.getString("name"), rs.getString("phone_number"),
                        rs.getString("email"), rs.getString("address"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    static void sortContacts() {
        try (Connection conn = getConnection()) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM contacts ORDER BY name ASC");

            System.out.println("\nSorted Contacts by Name:");
            while (rs.next()) {
                System.out.printf("ID: %d | Name: %s | Phone: %s | Email: %s | Address: %s\n",
                        rs.getInt("id"), rs.getString("name"), rs.getString("phone_number"),
                        rs.getString("email"), rs.getString("address"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    static void exportToCSV() {
        try (Connection conn = getConnection();
             PrintWriter writer = new PrintWriter(new File("contacts.csv"))) {
            StringBuilder sb = new StringBuilder();
            sb.append("ID,Name,Phone,Email,Address\n");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM contacts");
            while (rs.next()) {
                sb.append(rs.getInt("id")).append(",")
                        .append(rs.getString("name")).append(",")
                        .append(rs.getString("phone_number")).append(",")
                        .append(rs.getString("email")).append(",")
                        .append(rs.getString("address")).append("\n");
            }
            writer.write(sb.toString());
            System.out.println("Exported to contacts.csv successfully.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
