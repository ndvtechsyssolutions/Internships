table setup:

CREATE DATABASE contactdb;
USE contactdb;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(255)
);

Contact database application:

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;

public class SimpleContactBook extends JFrame {
    
    // Database connection details
    private static final String URL = "jdbc:mysql://localhost:3306/contactdb";
    private static final String USER = "root";
    private static final String PASS = "root@123";

    // GUI Components
    private JTextField nameField, phoneField, emailField, addressField;
    private JTextArea outputArea;
    private Connection conn;

    public SimpleContactBook() {
        setTitle("Contact Book");
        setSize(600, 400);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // Top input fields
        JPanel inputPanel = new JPanel(new GridLayout(4, 2));
        nameField = new JTextField(); phoneField = new JTextField();
        emailField = new JTextField(); addressField = new JTextField();

        inputPanel.add(new JLabel("Name:")); inputPanel.add(nameField);
        inputPanel.add(new JLabel("Phone:")); inputPanel.add(phoneField);
        inputPanel.add(new JLabel("Email:")); inputPanel.add(emailField);
        inputPanel.add(new JLabel("Address:")); inputPanel.add(addressField);
        add(inputPanel, BorderLayout.NORTH);

        // Buttons
        JPanel buttonPanel = new JPanel();
        JButton addBtn = new JButton("Add");
        JButton viewBtn = new JButton("View");
        JButton updateBtn = new JButton("Update");
        JButton deleteBtn = new JButton("Delete");
        buttonPanel.add(addBtn); buttonPanel.add(viewBtn);
        buttonPanel.add(updateBtn); buttonPanel.add(deleteBtn);
        add(buttonPanel, BorderLayout.CENTER);

        // Output area
        outputArea = new JTextArea();
        outputArea.setEditable(false);
        add(new JScrollPane(outputArea), BorderLayout.SOUTH);

        // Connect to DB
        try {
            conn = DriverManager.getConnection(URL, USER, PASS);
        } catch (SQLException e) {
            showMessage("Database Error: " + e.getMessage());
        }

        // Button actions
        addBtn.addActionListener(e -> addContact());
        viewBtn.addActionListener(e -> viewContacts());
        updateBtn.addActionListener(e -> updateContact());
        deleteBtn.addActionListener(e -> deleteContact());

        setVisible(true);
    }

    void addContact() {
        try (PreparedStatement stmt = conn.prepareStatement(
            "INSERT INTO contacts(name, phone, email, address) VALUES (?, ?, ?, ?)")) {
            stmt.setString(1, nameField.getText());
            stmt.setString(2, phoneField.getText());
            stmt.setString(3, emailField.getText());
            stmt.setString(4, addressField.getText());
            stmt.executeUpdate();
            showMessage("Contact added!");
        } catch (SQLException e) {
            showMessage("Add Error: " + e.getMessage());
        }
    }

    void viewContacts() {
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM contacts")) {
            outputArea.setText("");
            while (rs.next()) {
                outputArea.append("ID: " + rs.getInt("id") +
                    ", Name: " + rs.getString("name") +
                    ", Phone: " + rs.getString("phone") +
                    ", Email: " + rs.getString("email") +
                    ", Address: " + rs.getString("address") + "\n");
            }
        } catch (SQLException e) {
            showMessage("View Error: " + e.getMessage());
        }
    }

    void updateContact() {
        try (PreparedStatement stmt = conn.prepareStatement(
            "UPDATE contacts SET phone=?, email=?, address=? WHERE name=?")) {
            stmt.setString(1, phoneField.getText());
            stmt.setString(2, emailField.getText());
            stmt.setString(3, addressField.getText());
            stmt.setString(4, nameField.getText());
            int rows = stmt.executeUpdate();
            showMessage(rows > 0 ? "Contact updated!" : "No such contact.");
        } catch (SQLException e) {
            showMessage("Update Error: " + e.getMessage());
        }
    }

    void deleteContact() {
        try (PreparedStatement stmt = conn.prepareStatement(
            "DELETE FROM contacts WHERE name=?")) {
            stmt.setString(1, nameField.getText());
            int rows = stmt.executeUpdate();
            showMessage(rows > 0 ? "Contact deleted!" : "No such contact.");
        } catch (SQLException e) {
            showMessage("Delete Error: " + e.getMessage());
        }
    }

    void showMessage(String msg) {
        JOptionPane.showMessageDialog(this, msg);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SimpleContactBook::new);
    }
}
