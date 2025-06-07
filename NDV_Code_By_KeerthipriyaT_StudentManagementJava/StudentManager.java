import java.util.ArrayList;
import java.util.Scanner;

public class StudentManager {
    static ArrayList<Student> students = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;

        do {
            System.out.println("\n--- Student Management System ---");
            System.out.println("1. Add Student");
            System.out.println("2. View Students");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1 -> addStudent();
                case 2 -> viewStudents();
                case 3 -> updateStudent();
                case 4 -> deleteStudent();
                case 5 -> System.out.println("Thank you for using the system!");
                default -> System.out.println("Invalid choice.");
            }
        } while (choice != 5);
    }

    static void addStudent() {
        System.out.print("Enter ID: ");
        String id = sc.nextLine();

        for (Student s : students) {
            if (s.studentId.equals(id)) {
                System.out.println("Student with this ID already exists.");
                return;
            }
        }

        System.out.print("Enter Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Branch: ");
        String branch = sc.nextLine();
        System.out.print("Enter Year: ");
        int year = sc.nextInt();
        System.out.print("Enter Marks: ");
        double marks = sc.nextDouble();
        sc.nextLine();

        students.add(new Student(id, name, branch, year, marks));
        System.out.println("Student added.");
    }

    static void viewStudents() {
        if (students.isEmpty()) {
            System.out.println("No students to show.");
            return;
        }
        for (Student s : students) {
            s.display();
        }
    }

    static void updateStudent() {
        System.out.print("Enter ID to update: ");
        String id = sc.nextLine();

        for (Student s : students) {
            if (s.studentId.equals(id)) {
                System.out.print("Enter New Name: ");
                s.name = sc.nextLine();
                System.out.print("Enter New Branch: ");
                s.branch = sc.nextLine();
                System.out.print("Enter New Year: ");
                s.year = sc.nextInt();
                System.out.print("Enter New Marks: ");
                s.marks = sc.nextDouble();
                sc.nextLine();
                System.out.println("Student updated.");
                return;
            }
        }
        System.out.println("Student not found.");
    }

    static void deleteStudent() {
        System.out.print("Enter ID to delete: ");
        String id = sc.nextLine();

        for (Student s : students) {
            if (s.studentId.equals(id)) {
                students.remove(s);
                System.out.println("Student deleted.");
                return;
            }
        }
        System.out.println("Student not found.");
    }
}
