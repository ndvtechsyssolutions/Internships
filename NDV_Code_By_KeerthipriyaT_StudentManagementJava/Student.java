public class Student {
    String studentId;
    String name;
    String branch;
    int year;
    double marks;

    public Student(String studentId, String name, String branch, int year, double marks) {
        this.studentId = studentId;
        this.name = name;
        this.branch = branch;
        this.year = year;
        this.marks = marks;
    }

    public void display() {
        System.out.println("ID: " + studentId + ", Name: " + name + ", Branch: " + branch +
                           ", Year: " + year + ", Marks: " + marks);
    }
}
