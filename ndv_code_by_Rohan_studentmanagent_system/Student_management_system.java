public class Student {
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

    // Getters and Setters
    public String getStudentId() { return studentId; }
    public String getName() { return name; }
    public String getBranch() { return branch; }
    public int getYear() { return year; }
    public double getMarks() { return marks; }

    public void setName(String name) { this.name = name; }
    public void setBranch(String branch) { this.branch = branch; }
    public void setYear(int year) { this.year = year; }
    public void setMarks(double marks) { this.marks = marks; }

    @Override
    public String toString() {
        return "ID: " + studentId + ", Name: " + name + ", Branch: " + branch +
               ", Year: " + year + ", Marks: " + marks;
    }
}
