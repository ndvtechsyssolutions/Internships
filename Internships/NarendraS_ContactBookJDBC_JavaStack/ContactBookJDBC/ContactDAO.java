import java.sql.*;
import java.util.*;
import java.io.*;

public class ContactDAO {
    private Connection conn;

    public ContactDAO() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/contact_book", "contactuser", "contactpass");
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    public void addContact(Contact c) {
        if (conn == null) {
            System.err.println("Database connection failed. Cannot add contact.");
            return;
        }
        try {
            String sql = "INSERT INTO contacts (name, phone_number, email, address) VALUES (?, ?, ?, ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, c.getName());
            stmt.setString(2, c.getPhoneNumber());
            stmt.setString(3, c.getEmail());
            stmt.setString(4, c.getAddress());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Contact> getAllContacts() {
        List<Contact> list = new ArrayList<>();
        try {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM contacts");
            while (rs.next()) {
                list.add(new Contact(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("phone_number"),
                    rs.getString("email"),
                    rs.getString("address")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return list;
    }

    public void updateContact(Contact c) {
        try {
            String sql = "UPDATE contacts SET name=?, phone_number=?, email=?, address=? WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, c.getName());
            stmt.setString(2, c.getPhoneNumber());
            stmt.setString(3, c.getEmail());
            stmt.setString(4, c.getAddress());
            stmt.setInt(5, c.getId());
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteContact(int id) {
        try {
            String sql = "DELETE FROM contacts WHERE id=?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);
            stmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Contact> searchContact(String keyword) {
        List<Contact> list = new ArrayList<>();
        try {
            String sql = "SELECT * FROM contacts WHERE name LIKE ? OR phone_number LIKE ?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, "%" + keyword + "%");
            stmt.setString(2, "%" + keyword + "%");
            ResultSet rs = stmt.executeQuery();
            while (rs.next()) {
                list.add(new Contact(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getString("phone_number"),
                    rs.getString("email"),
                    rs.getString("address")
                ));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return list;
    }

    public void exportToCSV(String filename) {
        try (PrintWriter writer = new PrintWriter(new File(filename))) {
            StringBuilder sb = new StringBuilder();
            sb.append("ID,Name,Phone,Email,Address\n");
            List<Contact> contacts = getAllContacts();
            for (Contact c : contacts) {
                sb.append(c.getId()).append(",")
                  .append(c.getName()).append(",")
                  .append(c.getPhoneNumber()).append(",")
                  .append(c.getEmail()).append(",")
                  .append(c.getAddress()).append("\n");
            }
            writer.write(sb.toString());
            System.out.println("Exported successfully to " + filename);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}