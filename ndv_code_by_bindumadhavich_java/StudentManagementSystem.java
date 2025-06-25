import java.io.*;
import java.util.*;

class Student implements Serializable {
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

    public String getStudentId() {
        return studentId;
    }

    public String getName() {
        return name;
    }

    public String getBranch() {
        return branch;
    }

    public int getYear() {
        return year;
    }

    public double getMarks() {
        return marks;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public void setMarks(double marks) {
        this.marks = marks;
    }

    public String toString() {
        return "ID: " + studentId + ", Name: " + name + ", Branch: " + branch +
               ", Year: " + year + ", Marks: " + marks;
    }
}

class StudentManager {
    private HashMap<String, Student> students = new HashMap<>();
    private Scanner scanner = new Scanner(System.in);
    private final String DATA_FILE = "students.dat";

    public StudentManager() {
        loadFromFile();
    }

    public void start() {
        while (true) {
            System.out.println("\n=== Student Management System ===");
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Search Student");
            System.out.println("6. Show Statistics");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");

            String choice = scanner.nextLine().trim();
            switch (choice) {
                case "1": addStudent(); break;
                case "2": viewStudents(); break;
                case "3": updateStudent(); break;
                case "4": deleteStudent(); break;
                case "5": searchStudent(); break;
                case "6": showStatistics(); break;
                case "7": saveToFile(); System.out.println("Exiting..."); return;
                default: System.out.println("Invalid choice! Try again.");
            }
        }
    }

    private void addStudent() {
        System.out.print("Enter Student ID: ");
        String id = scanner.nextLine().trim();
        if (students.containsKey(id)) {
            System.out.println("Student ID already exists.");
            return;
        }

        System.out.print("Enter Name: ");
        String name = scanner.nextLine().trim();

        System.out.print("Enter Branch: ");
        String branch = scanner.nextLine().trim();

        int year = getIntInput("Enter Year (1-4): ", 1, 4);
        double marks = getDoubleInput("Enter Marks (0-100): ", 0, 100);

        Student student = new Student(id, name, branch, year, marks);
        students.put(id, student);
        System.out.println("Student added successfully.");
    }

    private void viewStudents() {
        if (students.isEmpty()) {
            System.out.println("No student records found.");
            return;
        }
        System.out.println("\n--- Student Records ---");
        for (Student s : students.values()) {
            System.out.println(s);
        }
    }

    private void updateStudent() {
        System.out.print("Enter Student ID to update: ");
        String id = scanner.nextLine().trim();
        Student s = students.get(id);
        if (s == null) {
            System.out.println("Student not found.");
            return;
        }

        System.out.print("Enter New Name: ");
        s.setName(scanner.nextLine().trim());

        System.out.print("Enter New Branch: ");
        s.setBranch(scanner.nextLine().trim());

        s.setYear(getIntInput("Enter New Year (1-4): ", 1, 4));
        s.setMarks(getDoubleInput("Enter New Marks (0-100): ", 0, 100));

        System.out.println("Student updated successfully.");
    }

    private void deleteStudent() {
        System.out.print("Enter Student ID to delete: ");
        String id = scanner.nextLine().trim();
        if (students.remove(id) != null) {
            System.out.println("Student deleted.");
        } else {
            System.out.println("Student ID not found.");
        }
    }

    private void searchStudent() {
        System.out.print("Enter Name or ID to search: ");
        String input = scanner.nextLine().trim().toLowerCase();

        boolean found = false;
        for (Student s : students.values()) {
            if (s.getStudentId().toLowerCase().equals(input) || s.getName().toLowerCase().contains(input)) {
                System.out.println(s);
                found = true;
            }
        }

        if (!found) System.out.println("No student found.");
    }

    private void showStatistics() {
        if (students.isEmpty()) {
            System.out.println("No data available.");
            return;
        }

        double totalMarks = 0;
        Student topStudent = null;

        for (Student s : students.values()) {
            totalMarks += s.getMarks();
            if (topStudent == null || s.getMarks() > topStudent.getMarks()) {
                topStudent = s;
            }
        }

        double average = totalMarks / students.size();
        System.out.println("Average Marks: " + average);
        System.out.println("Top Scorer: " + topStudent);
    }

    private int getIntInput(String msg, int min, int max) {
        while (true) {
            System.out.print(msg);
            try {
                int val = Integer.parseInt(scanner.nextLine().trim());
                if (val >= min && val <= max) return val;
                System.out.println("Please enter a number between " + min + " and " + max + ".");
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Try again.");
            }
        }
    }

    private double getDoubleInput(String msg, double min, double max) {
        while (true) {
            System.out.print(msg);
            try {
                double val = Double.parseDouble(scanner.nextLine().trim());
                if (val >= min && val <= max) return val;
                System.out.println("Please enter a number between " + min + " and " + max + ".");
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Try again.");
            }
        }
    }

    @SuppressWarnings("unchecked")
    private void loadFromFile() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(DATA_FILE))) {
            students = (HashMap<String, Student>) ois.readObject();
            System.out.println("Loaded student data from file.");
        } catch (Exception e) {
            students = new HashMap<>();
            System.out.println("No previous data found. Starting fresh.");
        }
    }

    private void saveToFile() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(DATA_FILE))) {
            oos.writeObject(students);
            System.out.println("Data saved to file.");
        } catch (IOException e) {
            System.out.println("Error saving data.");
        }
    }
}

public class StudentManagementSystem {
    public static void main(String[] args) {
        new StudentManager().start();
    }
}
