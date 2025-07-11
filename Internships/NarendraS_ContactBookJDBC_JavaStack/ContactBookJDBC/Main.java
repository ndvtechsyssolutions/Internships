import java.util.*;
import java.util.regex.*;

public class Main {
    public static boolean isValidEmail(String email) {
        return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
    }

    public static boolean isValidPhone(String phone) {
        return phone.matches("^[0-9]{10}$");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ContactDAO dao = new ContactDAO();
        int choice=-1;

        do {
            System.out.println("\n--- Contact Book Menu ---");
            System.out.println("1. Add Contact");
            System.out.println("2. View All Contacts");
            System.out.println("3. Update Contact");
            System.out.println("4. Delete Contact");
            System.out.println("5. Search Contact");
            System.out.println("6. Export to CSV");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");

            if (!sc.hasNextInt()) {
                System.out.println("Invalid input. Please enter a number between 1 and 7.");
                sc.next();
                continue;
            }

            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Name: "); String name = sc.nextLine();
                    String phone;
                    do {
                        System.out.print("Phone (10 digits): ");
                        phone = sc.nextLine();
                    } while (!isValidPhone(phone));

                    String email;
                    do {
                        System.out.print("Email: ");
                        email = sc.nextLine();
                    } while (!isValidEmail(email));

                    System.out.print("Address: "); String address = sc.nextLine();
                    dao.addContact(new Contact(name, phone, email, address));
                    break;
                case 2:
                    List<Contact> contacts = dao.getAllContacts();
                    contacts.forEach(System.out::println);
                    break;
                case 3:
                    System.out.print("Enter ID to update: "); int idUp = sc.nextInt(); sc.nextLine();
                    System.out.print("New Name: "); name = sc.nextLine();

                    do {
                        System.out.print("New Phone (10 digits): ");
                        phone = sc.nextLine();
                    } while (!isValidPhone(phone));

                    do {
                        System.out.print("New Email: ");
                        email = sc.nextLine();
                    } while (!isValidEmail(email));

                    System.out.print("New Address: "); address = sc.nextLine();
                    dao.updateContact(new Contact(idUp, name, phone, email, address));
                    break;
                case 4:
                    System.out.print("Enter ID to delete: "); int idDel = sc.nextInt();
                    dao.deleteContact(idDel);
                    break;
                case 5:
                    System.out.print("Enter name or phone to search: "); String key = sc.nextLine();
                    List<Contact> found = dao.searchContact(key);
                    found.forEach(System.out::println);
                    break;
                case 6:
                    dao.exportToCSV("contacts.csv");
                    break;
                case 7:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please select between 1 and 7.");
            }
        }while(choice !=7);
        sc.close();
    }
}
