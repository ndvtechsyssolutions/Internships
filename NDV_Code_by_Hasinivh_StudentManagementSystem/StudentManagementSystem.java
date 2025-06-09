import java.util.ArrayList;
import java.util.Scanner;

class Student {
    int rollNo;
    String name;
    String course;
    double marks;
    String email;
    String phoneNo;
    String address;
    String gender; 
  
    public Student(int rollNo, String name, String course, double marks,
                   String email, String phoneNo, String address, String gender) {
        this.rollNo = rollNo;
        this.name = name;
        this.course = course;
        this.marks = marks;
        this.email = email;
        this.phoneNo = phoneNo;
        this.address = address;
        this.gender = gender;
    }
    public void displayInfo() {
        System.out.println("Roll No : " + rollNo);
        System.out.println("Name    : " + name);
        System.out.println("Course  : " + course);
        System.out.println("Marks   : " + marks);
        System.out.println("Email   : " + email);
        System.out.println("Phone   : " + phoneNo);
        System.out.println("Address : " + address);
        System.out.println("Gender  : " + gender);
    }
}

public class StudentManagementSystem {

    static ArrayList<Student> students = new ArrayList<>();
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int choice;

        do {
            System.out.println("1. Add Student");
            System.out.println("2. Display All Students");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    addStudent();
                    break;
                case 2:
                    displayStudents();
                    break;
                case 3:
                    System.out.println("Exiting... Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }

        } while (choice != 3);
    }

    static void addStudent() {
        System.out.print("Enter Roll No: ");
        int rollNo = sc.nextInt();
        sc.nextLine(); // clear buffer

        System.out.print("Enter Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Course: ");
        String course = sc.nextLine();

        System.out.print("Enter Marks: ");
        double marks = sc.nextDouble();
        sc.nextLine(); // clear buffer

        System.out.print("Enter Email: ");
        String email = sc.nextLine();

        System.out.print("Enter Phone No: ");
        String phoneNo = sc.nextLine();

        System.out.print("Enter Address: ");
        String address = sc.nextLine();

        System.out.print("Enter Gender: ");
        String gender = sc.nextLine();
      
        Student student = new Student(rollNo, name, course, marks, email, phoneNo, address, gender);
        students.add(student);

        System.out.println(" Student added successfully!");
    }

    static void displayStudents() {
        if (students.isEmpty()) {
            System.out.println(" No students yet.");
            return;
        }

        for (Student s : students) {
            s.displayInfo();
        }
    }
}
