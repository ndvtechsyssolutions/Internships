import java.util.*;
import java.io.*;

class Student implements Serializable {
    private int id;
    private String name;
    private int age;
    private String course;

    public Student(int id, String name, int age, String course) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.course = course;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public int getAge() { return age; }
    public String getCourse() { return course; }
    public void setName(String name) { this.name = name; }
    public void setAge(int age) { this.age = age; }
    public void setCourse(String course) { this.course = course; }

    public String toString() {
        return id + " | " + name + " | " + age + " | " + course;
    }
}

class StudentManager {
    private List<Student> students;
    private final String FILE_NAME = "students.dat";

    public StudentManager() {
        students = new ArrayList<>();
        loadStudents();
    }

    public void addStudent(Student s) {
        students.add(s);
        saveStudents();
    }

    public void displayAll() {
        for (Student s : students) {
            System.out.println(s);
        }
    }

    public Student findStudent(int id) {
        for (Student s : students) {
            if (s.getId() == id) return s;
        }
        return null;
    }

    public void deleteStudent(int id) {
        students.removeIf(s -> s.getId() == id);
        saveStudents();
    }

    public void updateStudent(int id, String name, int age, String course) {
        Student s = findStudent(id);
        if (s != null) {
            s.setName(name);
            s.setAge(age);
            s.setCourse(course);
            saveStudents();
        }
    }

    private void loadStudents() {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(FILE_NAME))) {
            students = (List<Student>) in.readObject();
        } catch (Exception e) {
            students = new ArrayList<>();
        }
    }

    private void saveStudents() {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(FILE_NAME))) {
            out.writeObject(students);
        } catch (Exception e) {
            System.out.println("Error saving student data.");
        }
    }
}

public class StudentManagementSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StudentManager manager = new StudentManager();
        while (true) {
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Search Student by ID");
            System.out.println("4. Update Student");
            System.out.println("5. Delete Student");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            int choice = Integer.parseInt(sc.nextLine());

            if (choice == 1) {
                System.out.print("Enter ID: ");
                int id = Integer.parseInt(sc.nextLine());
                System.out.print("Enter Name: ");
                String name = sc.nextLine();
                System.out.print("Enter Age: ");
                int age = Integer.parseInt(sc.nextLine());
                System.out.print("Enter Course: ");
                String course = sc.nextLine();
                manager.addStudent(new Student(id, name, age, course));
            } else if (choice == 2) {
                manager.displayAll();
            } else if (choice == 3) {
                System.out.print("Enter ID: ");
                int id = Integer.parseInt(sc.nextLine());
                Student s = manager.findStudent(id);
                if (s != null) System.out.println(s);
                else System.out.println("Student not found");
            } else if (choice == 4) {
                System.out.print("Enter ID to update: ");
                int id = Integer.parseInt(sc.nextLine());
                System.out.print("Enter New Name: ");
                String name = sc.nextLine();
                System.out.print("Enter New Age: ");
                int age = Integer.parseInt(sc.nextLine());
                System.out.print("Enter New Course: ");
                String course = sc.nextLine();
                manager.updateStudent(id, name, age, course);
            } else if (choice == 5) {
                System.out.print("Enter ID to delete: ");
                int id = Integer.parseInt(sc.nextLine());
                manager.deleteStudent(id);
            } else if (choice == 6) {
                break;
            } else {
                System.out.println("Invalid choice");
            }
        }
    }
}
