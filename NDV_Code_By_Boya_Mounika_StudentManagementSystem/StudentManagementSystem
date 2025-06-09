// Import necessary classes for input and dynamic list handling
import java.util.ArrayList;
import java.util.Scanner;

// Student class to hold individual student details
class Student {
    int rollNo;
    String name;
    String course;
    double marks;

    // Constructor to initialize student object
    public Student(int rollNo, String name, String course, double marks) {
        this.rollNo = rollNo;
        this.name = name;
        this.course = course;
        this.marks = marks;
    }

    // Method to display student details
    public void display() {
        System.out.println("Roll No: " + rollNo + ", Name: " + name + ", Course: " + course + ", Marks: " + marks);
    }
}

// Main class to manage the student system
public class StudentManagementSystem {

    // List to store all student records
    static ArrayList<Student> students = new ArrayList<>();

    // Scanner object to take user input
    static Scanner sc = new Scanner(System.in);

    // Entry point of the program
    public static void main(String[] args) {
        int choice = -1; // Initialize choice to avoid compilation issues

        // Loop to show menu and take actions until user exits
        do {
            // Display the menu
            System.out.println("\n-- Student Management System --");
            System.out.println("1. Add Student");
            System.out.println("2. Display All Students");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            // Read user's menu choice
            choice = sc.nextInt();
            sc.nextLine(); // Clear buffer (to avoid input skipping issues)

            // Perform action based on user's choice
            switch (choice) {
                case 1:
                    addStudent(); // Add a new student
                    break;
                case 2:
                    displayStudents(); // Display all students
                    break;
                case 3:
                    System.out.println("Goodbye!"); // Exit message
                    break;
                default:
                    System.out.println("Invalid choice."); // Handle invalid inputs
            }
        } while (choice != 3); // Repeat menu until user chooses to exit
    }

    // Method to collect student details and add to the list
    static void addStudent() {
        System.out.print("Enter Roll No: ");
        int rollNo = sc.nextInt();
        sc.nextLine(); // Clear buffer

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Course: ");
        String course = sc.nextLine();

        System.out.print("Enter Marks: ");
        double marks = sc.nextDouble();

        // Create new student and add to the list
        students.add(new Student(rollNo, name, course, marks));
        System.out.println("Student added!");
    }

    // Method to display all stored student records
    static void displayStudents() {
        // Check if list is empty
        if (students.isEmpty()) {
            System.out.println("No students yet.");
            return;
        }

        // Loop through each student and display their info
        for (Student s : students) {
            s.display();
        }
    }
}
