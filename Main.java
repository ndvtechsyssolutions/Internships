import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        StudentManager manager = new StudentManager();
        manager.addStudent(1, "John", "CS", 2, 85.0);
        manager.addStudent(2, "Mary", "EE", 3, 90.5);
        System.out.println("\nAll Students:");
        manager.viewAllStudents();
        System.out.println("\nView Student ID 1:");
        manager.viewStudent(1);
        System.out.println("\nUpdate Student ID 1:");
        manager.updateStudent(1, "John Smith", "CS", 2, 88.0);
        System.out.println("\nAll Students after update:");
        manager.viewAllStudents();
        System.out.println("\nDelete Student ID 2:");
        manager.deleteStudent(2);
        System.out.println("\nAll Students after deletion:");
        manager.viewAllStudents();
    }
}

class Student {
    int id;
    String name;
    String branch;
    int year;
    double marks;

    Student(int id, String name, String branch, int year, double marks) {
        this.id = id;
        this.name = name;
        this.branch = branch;
        this.year = year;
        this.marks = marks;
    }

    public String toString() {
        return "ID: " + id + ", Name: " + name + ", Branch: " + branch + ", Year: " + year + ", Marks: " + marks;
    }
}

class StudentManager {
    private ArrayList<Student> students = new ArrayList<>();

    void addStudent(int id, String name, String branch, int year, double marks) {
        students.add(new Student(id, name, branch, year, marks));
        System.out.println("Student added: " + name);
    }

    void updateStudent(int id, String name, String branch, int year, double marks) {
        for (Student s : students) {
            if (s.id == id) {
                s.name = name;
                s.branch = branch;
                s.year = year;
                s.marks = marks;
                System.out.println("Student updated: " + name);
                return;
            }
        }
        System.out.println("Student ID " + id + " not found");
    }

    void viewStudent(int id) {
        for (Student s : students) {
            if (s.id == id) {
                System.out.println(s);
                return;
            }
        }
        System.out.println("Student ID " + id + " not found");
    }

    void viewAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No students found");
        } else {
            for (Student s : students) {
                System.out.println(s);
            }
        }
    }

    void deleteStudent(int id) {
        for (int i = 0; i < students.size(); i++) {
            if (students.get(i).id == id) {
                System.out.println("Student deleted: " + students.get(i).name);
                students.remove(i);
                return;
            }
        }
        System.out.println("Student ID " + id + " not found");
    }
}
