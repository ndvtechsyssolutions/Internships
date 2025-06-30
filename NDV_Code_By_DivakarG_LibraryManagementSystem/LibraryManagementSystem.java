import java.sql.*;
import java.util.*; 

public class LibraryManager {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\n Library Management System"); 
            System.out.println("1. Add Book");
            System.out.println("2. View All Books");
            System.out.println("3. Search Book by Title");
            System.out.println("4. Delete Book by ID");
            System.out.println("5. Exit");
            System.out.print("Choose: ");
            int choice = sc.nextInt();
            sc.nextLine(); // clear newline

            switch (choice) {
                case 1 -> addBook(sc);
                case 2 -> viewBooks();
                case 3 -> searchBook(sc);
                case 4 -> deleteBook(sc);
                case 5 -> {
                    System.out.println("Thank you! Exiting...");
                    System.exit(0);
                }
                default -> System.out.println("Invalid choice.");
            }
        }
    }

    static void addBook(Scanner sc) {
        try (Connection conn = DBConnection.getConnection()) {
            System.out.print("Enter Title: ");
            String title = sc.nextLine();
            System.out.print("Enter Author: ");
            String author = sc.nextLine();
            System.out.print("Enter Year: ");
            int year = sc.nextInt();

            String sql = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, title);
            stmt.setString(2, author);
            stmt.setInt(3, year);
            stmt.executeUpdate();
            System.out.println(" Book added successfully!"); 
        } catch (Exception e) {
            System.out.println(" Error: " + e.getMessage()); 
        }
    }

    static void viewBooks() {
        try (Connection conn = DBConnection.getConnection()) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM books");
            System.out.printf("%-5s %-30s %-20s %-5s\n", "ID", "Title", "Author", "Year");
            while (rs.next()) {
                System.out.printf("%-5d %-30s %-20s %-5d\n",
                        rs.getInt("id"), rs.getString("title"),
                        rs.getString("author"), rs.getInt("year"));
            }
        } catch (Exception e) {
            System.out.println(" Error: " + e.getMessage()); 
        }
    }

    static void searchBook(Scanner sc) {
        try (Connection conn = DBConnection.getConnection()) {
            System.out.print("Enter book title to search: ");
            String title = sc.nextLine();

            String sql = "SELECT * FROM books WHERE title LIKE ?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, "%" + title + "%");
            ResultSet rs = stmt.executeQuery();

            while (rs.next()) {
                System.out.printf("Found -> ID: %d, Title: %s, Author: %s, Year: %d\n",
                        rs.getInt("id"), rs.getString("title"),
                        rs.getString("author"), rs.getInt("year"));
            }
        } catch (Exception e) {
            System.out.println(" Error: " + e.getMessage()); 
        }
    }

    static void deleteBook(Scanner sc) {
        try (Connection conn = DBConnection.getConnection()) {
            System.out.print("Enter Book ID to delete: ");
            int id = sc.nextInt();

            String sql = "DELETE FROM books WHERE id = ?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setInt(1, id);
            int rows = stmt.executeUpdate();

            if (rows > 0)
                System.out.println(" Book deleted successfully!"); 
            else
                System.out.println(" No book found with that ID."); 
        } catch (Exception e) {
            System.out.println(" Error: " + e.getMessage()); 
        }
    }
}
