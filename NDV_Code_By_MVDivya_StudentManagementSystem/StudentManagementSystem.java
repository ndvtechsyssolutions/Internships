import java.util.ArrayList;
import java.util.Scanner;

class Student {
    int serialNo;
    int rollNo;
    String name;
    String subject;
    double marks;

    public Student(int serialNo, int rollNo, String name, String subject, double marks) {
        this.serialNo = serialNo;
        this.rollNo = rollNo;
        this.name = name;
        this.subject = subject;
        this.marks = marks;
    }

    public void display() {
        System.out.println("S.No: " + serialNo + ", Roll No: " + rollNo + ", Name: " + name + ", Subject: " + subject + ", Marks: " + marks);
    }
}

public class StudentManagementSystem {
    static ArrayList<Student> students = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n-- Student Management System --");
            System.out.println("1. Add Student");
            System.out.println("2. Display All Students");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    displayStudents();
                    break;
                case 3:
                    System.out.println("Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 3);
    }

    static void addStudent() {
        System.out.print("Enter S.No: ");
        int serialNo = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Roll No: ");
        int rollNo = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Subject: ");
        String subject = sc.nextLine();

        System.out.print("Enter Marks: ");
        double marks = sc.nextDouble();

        students.add(new Student(serialNo, rollNo, name, subject, marks));
        System.out.println("Student added!");
    }

    static void displayStudents() {
        if (students.isEmpty()) {
            System.out.println("No students yet.");
            return;
        }
        for (Student s : students) {
            s.display();
        }
    }
}
