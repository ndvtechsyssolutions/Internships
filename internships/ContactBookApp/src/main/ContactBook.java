package main;

import dao.ContactDAO;
import model.Contact;

import java.util.List;
import java.util.Scanner;

public class ContactBook {
    public static void main(String[] args) {
        ContactDAO contactDAO = new ContactDAO();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nContact Book Menu:");
            System.out.println("1. Add Contact");
            System.out.println("2. View All Contacts");
            System.out.println("3. Update Contact");
            System.out.println("4. Delete Contact");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.println("Enter Contact Details:");
                    System.out.print("Name: ");
                    String name = scanner.nextLine();
                    System.out.print("Phone Number: ");
                    String phoneNumber = scanner.nextLine();
                    System.out.print("Email: ");
                    String email = scanner.nextLine();
                    System.out.print("Address: ");
                    String address = scanner.nextLine();

                    Contact contact = new Contact(0, name, phoneNumber, email, address);
                    contactDAO.addContact(contact);
                    break;

                case 2:
                    List<Contact> contacts = contactDAO.getAllContacts();
                    contacts.forEach(c -> System.out.println(c.getId() + ". " + c.getName() + " - " + c.getPhoneNumber() + " - " + c.getEmail() + " - " + c.getAddress()));
                    break;

                case 3:
                    System.out.print("Enter Contact ID to update: ");
                    int updateId = scanner.nextInt();
                    scanner.nextLine();

                    System.out.println("Enter New Details:");
                    System.out.print("Name: ");
                    String newName = scanner.nextLine();
                    System.out.print("Phone Number: ");
                    String newPhoneNumber = scanner.nextLine();
                    System.out.print("Email: ");
                    String newEmail = scanner.nextLine();
                    System.out.print("Address: ");
                    String newAddress = scanner.nextLine();

                    Contact updatedContact = new Contact(updateId, newName, newPhoneNumber, newEmail, newAddress);
                    contactDAO.updateContact(updatedContact);
                    break;

                case 4:
                    System.out.print("Enter Contact ID to delete: ");
                    int deleteId = scanner.nextInt();
                    contactDAO.deleteContact(deleteId);
                    break;

                case 5:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }
}
