package dao;

import model.Contact;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ContactDAO {
    private static final String URL = "jdbc:mysql://localhost:3306/contactbook";
    private static final String USER = "root";
    private static final String PASSWORD = "Mvgr@74322";

    public Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, "root","Mvgr@74322");
    }

    public void addContact(Contact contact) {
        String sql = "INSERT INTO contacts (name, phone_number, email, address) VALUES (?, ?, ?, ?)";
        try (Connection conn = getConnection(); PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, contact.getName());
            stmt.setString(2, contact.getPhoneNumber());
            stmt.setString(3, contact.getEmail());
            stmt.setString(4, contact.getAddress());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Contact> getAllContacts() {
        List<Contact> contacts = new ArrayList<>();
        String sql = "SELECT * FROM contacts";
        try (Connection conn = getConnection(); Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                Contact contact = new Contact(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("phone_number"),
                    rs.getString("email"),
                    rs.getString("address")
                );
                contacts.add(contact);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return contacts;
    }

    public void updateContact(Contact contact) {
        String sql = "UPDATE contacts SET name = ?, phone_number = ?, email = ?, address = ? WHERE id = ?";
        try (Connection conn = getConnection(); PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, contact.getName());
            stmt.setString(2, contact.getPhoneNumber());
            stmt.setString(3, contact.getEmail());
            stmt.setString(4, contact.getAddress());
            stmt.setInt(5, contact.getId());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteContact(int id) {
        String sql = "DELETE FROM contacts WHERE id = ?";
        try (Connection conn = getConnection(); PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
