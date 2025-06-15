import java.util.*;
class Student {
    private int rollNo;
    private String name;
    private int age;
    private String course;
public Student(int rollNo, String name, int age, String course) {
        this.rollNo = rollNo;
        this.name = name;
        this.age = age;
        this.course = course;
    }

public int getRollNo() {
        return rollNo;
    }
public void setName(String name) {
        this.name = name;
    }
  public void setAge(int age) {
        this.age = age;
    }
public void setCourse(String course) {
        this.course = course;
    }
  public void display() {
        System.out.println("Roll No: " + rollNo + ", Name: " + name +", Age: " + age + ", Course: " + course);
    }
}

public class StudentManagementSystem {
     private static Map<Integer, Student> studentMap = new HashMap<>();
    private static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
while (true) {
            System.out.println("\n==== Student Management System ====");
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Search Student by Roll No");
            System.out.println("4. Delete Student");
            System.out.println("5. Update Student");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
          int choice = sc.nextInt();
            switch (choice) {
                case 1 -> addStudent();
                case 2 -> viewStudents();
                case 3 -> searchStudent();
                case 4 -> deleteStudent();
                case 5 -> updateStudent();
                case 6 -> running = false;
                default -> System.out.println("Invalid choice!");
            }
        }
    }

    private static void addStudent() {
        System.out.print("Enter Roll No: ");
        int roll = sc.nextInt();
        sc.nextLine();
        if (studentMap.containsKey(roll)) {
            System.out.println("Student already exists!");
            return;
        }

        System.out.print("Enter Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Age: ");
        int age = sc.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.print("Enter Course: ");
        String course = sc.nextLine();
      Student student = new Student(roll, name, age, course);
        studentMap.put(roll, student);
        System.out.println("Student added successfully.");
    }

    private static void viewStudents() {
        if (studentMap.isEmpty()) {
            System.out.println("No students found.");
            return;
        }
      System.out.println("List of Students:");
        for (Student s : studentMap.values()) {
            s.display();
        }
    }
  private static void searchStudent() {
        System.out.print("Enter Roll No to search: ");
        int roll = sc.nextInt();
        Student student = studentMap.get(roll);
        if (student != null) {
            student.display();
        } else {
            System.out.println("Student not found!");
        }
    }
  private static void deleteStudent() {
        System.out.print("Enter Roll No to delete: ");
        int roll = sc.nextInt();
        if (studentMap.remove(roll) != null) {
            System.out.println("Student deleted successfully.");
        } else {
            System.out.println("Student not found!");
        }
    }

    private static void updateStudent() {
        System.out.print("Enter Roll No to update: ");
        int roll = sc.nextInt();
        Student student = studentMap.get(roll);
        if (student == null) {
            System.out.println("Student not found!");
            return;
        }
      sc.nextLine();
        System.out.print("Enter New Name: ");
        String name = sc.nextLine();
        System.out.print("Enter New Age: ");
        int age = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter New Course: ");
        String course = sc.nextLine();
      student.setName(name);
        student.setAge(age);
        student.setCourse(course);

        System.out.println("Student updated successfully.");
    }
    }
