import java.util.ArrayList;
import java.util.Scanner;

class Student {
    private String studentId;
    private String name;
    private String branch;
    private int year;
    private double marks;

    public Student(String studentId, String name, String branch, int year, double marks) {
        this.studentId = studentId;
        this.name = name;
        this.branch = branch;
        this.year = year;
        this.marks = marks;
    }

    public String getStudentId() { return studentId; }
    public String getName() { return name; }
    public String getBranch() { return branch; }
    public int getYear() { return year; }
    public double getMarks() { return marks; }

    public void setName(String name) { this.name = name; }
    public void setBranch(String branch) { this.branch = branch; }
    public void setYear(int year) { this.year = year; }
    public void setMarks(double marks) { this.marks = marks; }

    public void display() {
        System.out.println("ID: " + studentId + ", Name: " + name + ", Branch: " + branch + ", Year: " + year + ", Marks: " + marks);
    }
}

public class StudentManagementSystem {
    static ArrayList<Student> students = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;

        do {
            System.out.println("\n--- Student Management System ---");
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Top Scorer");
            System.out.println("6. Average Marks");
            System.out.println("0. Exit");
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
                    updateStudent();
                    break;
                case 4:
                    deleteStudent();
                    break;
                case 5:
                    showTopScorer();
                    break;
                case 6:
                    showAverageMarks();
                    break;
                case 0:
                    System.out.println("Exiting the system...");
                    break;
                default:
                    System.out.println("Invalid choice!");
            }

        } while (choice != 0);
    }

    static void addStudent() {
        System.out.print("Enter Student ID: ");
        String id = sc.nextLine();

        // Check for unique ID
        for (Student s : students) {
            if (s.getStudentId().equalsIgnoreCase(id)) {
                System.out.println("Student ID already exists!");
                return;
            }
        }

        System.out.print("Enter Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Branch: ");
        String branch = sc.nextLine();
        System.out.print("Enter Year (e.g., 1, 2, 3, 4): ");
        int year = sc.nextInt();
        System.out.print("Enter Marks: ");
        double marks = sc.nextDouble();
        sc.nextLine(); // consume newline

        if (marks < 0 || marks > 100) {
            System.out.println("Marks must be between 0 and 100.");
            return;
        }

        students.add(new Student(id, name, branch, year, marks));
        System.out.println("Student added successfully!");
    }

    static void displayStudents() {
        if (students.isEmpty()) {
            System.out.println("No student records found.");
            return;
        }
        for (Student s : students) {
            s.display();
        }
    }

    static void updateStudent() {
        System.out.print("Enter Student ID to update: ");
        String id = sc.nextLine();

        for (Student s : students) {
            if (s.getStudentId().equalsIgnoreCase(id)) {
                System.out.print("Enter new Name: ");
                s.setName(sc.nextLine());
                System.out.print("Enter new Branch: ");
                s.setBranch(sc.nextLine());
                System.out.print("Enter new Year: ");
                s.setYear(sc.nextInt());
                System.out.print("Enter new Marks: ");
                s.setMarks(sc.nextDouble());
                sc.nextLine(); // consume newline
                System.out.println("Student record updated!");
                return;
            }
        }

        System.out.println("Student not found.");
    }

    static void deleteStudent() {
        System.out.print("Enter Student ID to delete: ");
        String id = sc.nextLine();

        for (Student s : students) {
            if (s.getStudentId().equalsIgnoreCase(id)) {
                students.remove(s);
                System.out.println("Student deleted!");
                return;
            }
        }

        System.out.println("Student not found.");
    }

    static void showTopScorer() {
        if (students.isEmpty()) {
            System.out.println("No student data available.");
            return;
        }

        Student top = students.get(0);
        for (Student s : students) {
            if (s.getMarks() > top.getMarks()) {
                top = s;
            }
        }

        System.out.println("Top Scorer:");
        top.display();
    }

    static void showAverageMarks() {
        if (students.isEmpty()) {
            System.out.println("No student data available.");
            return;
        }

        double total = 0;
        for (Student s : students) {
            total += s.getMarks();
        }

        double avg = total / students.size();
        System.out.printf("Average Marks: %.2f\n", avg);
    }
}
