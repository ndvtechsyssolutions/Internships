import java.util.*;

class Student {
    int studentId;
    String name;
    String branch;
    int year;
    int marks;

    public Student(int studentId, String name, String branch, int year, int marks) {
        this.studentId = studentId;
        this.name = name;
        this.branch = branch;
        this.year = year;
        this.marks = marks;
    }

    public String toString() {
        return "ID: " + studentId + ", Name: " + name + ", Branch: " + branch + ", Year: " + year + ", Marks: " + marks;
    }
}

class StudentManager {
    private Map<Integer, Student> students;

    public StudentManager() {
        students = new HashMap<>();
    }

    public void addStudent(Student student) {
        students.put(student.studentId, student);
        System.out.println("Student added: " + student);
    }

    public void viewStudent(int studentId) {
        if (students.containsKey(studentId)) {
            System.out.println(students.get(studentId));
        } else {
            System.out.println("Student not found.");
        }
    }

    public void updateStudent(int studentId, String name, String branch, int year, int marks) {
        if (students.containsKey(studentId)) {
            Student student = students.get(studentId);
            student.name = name;
            student.branch = branch;
            student.year = year;
            student.marks = marks;
            System.out.println("Student updated: " + student);
        } else {
            System.out.println("Student not found.");
        }
    }

    public void deleteStudent(int studentId) {
        if (students.containsKey(studentId)) {
            students.remove(studentId);
            System.out.println("Student deleted.");
        } else {
            System.out.println("Student not found.");
        }
    }

    public void displayTopScorer() {
        if (students.isEmpty()) {
            System.out.println("No students to display.");
            return;
        }
        Student topScorer = Collections.max(students.values(), Comparator.comparingInt(s -> s.marks));
        System.out.println("Top Scorer: " + topScorer);
    }

    public void displayAverageMarks() {
        if (students.isEmpty()) {
            System.out.println("No students to calculate.");
            return;
        }
        double average = students.values().stream().mapToInt(s -> s.marks).average().orElse(0.0);
        System.out.println("Average Marks: " + average);
    }
}

public class StudentManagementSystem {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StudentManager manager = new StudentManager();
        int choice;
        
        do {
            System.out.println("\nStudent Management System");
            System.out.println("1. Add Student");
            System.out.println("2. View Student");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. View Top Scorer");
            System.out.println("6. View Average Marks");
            System.out.println("7. Exit");
            System.out.print("Choose an option: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    // Add Student
                    System.out.print("Enter student ID: ");
                    int id = scanner.nextInt();
                    scanner.nextLine(); // consume newline
                    System.out.print("Enter student name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter student branch: ");
                    String branch = scanner.nextLine();
                    System.out.print("Enter student year: ");
                    int year = scanner.nextInt();
                    System.out.print("Enter student marks: ");
                    int marks = scanner.nextInt();
                    manager.addStudent(new Student(id, name, branch, year, marks));
                    break;
                case 2:
                    // View Student
                    System.out.print("Enter student ID to view: ");
                    int viewId = scanner.nextInt();
                    manager.viewStudent(viewId);
                    break;
                case 3:
                    // Update Student
                    System.out.print("Enter student ID to update: ");
                    int updateId = scanner.nextInt();
                    scanner.nextLine(); // consume newline
                    System.out.print("Enter new student name: ");
                    String newName = scanner.nextLine();
                    System.out.print("Enter new student branch: ");
                    String newBranch = scanner.nextLine();
                    System.out.print("Enter new student year: ");
                    int newYear = scanner.nextInt();
                    System.out.print("Enter new student marks: ");
                    int newMarks = scanner.nextInt();
                    manager.updateStudent(updateId, newName, newBranch, newYear, newMarks);
                    break;
                case 4:
                    // Delete Student
                    System.out.print("Enter student ID to delete: ");
                    int deleteId = scanner.nextInt();
                    manager.deleteStudent(deleteId);
                    break;
                case 5:
                    // Display Top Scorer
                    manager.displayTopScorer();
                    break;
                case 6:
                    // Display Average Marks
                    manager.displayAverageMarks();
                    break;
                case 7:
                    System.out.println("Exiting program.");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        } while (choice != 7);

        scanner.close();
    }
}
