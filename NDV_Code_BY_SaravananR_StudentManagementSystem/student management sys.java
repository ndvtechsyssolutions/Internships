import java.util.*;

public class StudentManagement {
    static class Student {
        private int studentId;
        private String name;
        private String branch;
        private int year;
        private double marks;

        public Student(int studentId, String name, String branch, int year, double marks) {
            this.studentId = studentId;
            this.name = name;
            this.branch = branch;
            this.year = year;
            this.marks = marks;
        }

        public int getStudentId() { return studentId; }
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
            return String.format("ID: %d | Name: %s | Branch: %s | Year: %d | Marks: %.2f",
                                 studentId, name, branch, year, marks);
        }
    }

    static class StudentManager {
        private Map<Integer, Student> students = new HashMap<>();

        public boolean addStudent(Student s) {
            if (students.containsKey(s.getStudentId())) return false;
            students.put(s.getStudentId(), s);
            return true;
        }

        public Collection<Student> getAllStudents() {
            return students.values();
        }

        public Student getStudentById(int id) {
            return students.get(id);
        }

        public boolean updateStudent(int id, String name, String branch, int year, double marks) {
            Student s = students.get(id);
            if (s == null) return false;
            s.setName(name);
            s.setBranch(branch);
            s.setYear(year);
            s.setMarks(marks);
            return true;
        }

        public boolean deleteStudent(int id) {
            return students.remove(id) != null;
        }

        public List<Student> searchByName(String namePart) {
            List<Student> result = new ArrayList<>();
            for (Student s : students.values()) {
                if (s.getName().toLowerCase().contains(namePart.toLowerCase())) {
                    result.add(s);
                }
            }
            return result;
        }

        public Optional<Student> getTopScorer() {
            return students.values().stream()
                    .max(Comparator.comparingDouble(Student::getMarks));
        }

        public double getAverageMarks() {
            return students.values().stream()
                    .mapToDouble(Student::getMarks)
                    .average()
                    .orElse(0.0);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StudentManager manager = new StudentManager();

        while (true) {
            System.out.println("\n=== Student Management System ===");
            System.out.println("1. Add Student");
            System.out.println("2. View All Students");
            System.out.println("3. Update Student");
            System.out.println("4. Delete Student");
            System.out.println("5. Search by Name");
            System.out.println("6. Show Statistics");
            System.out.println("7. Exit");
            System.out.print("Choose an option: ");
            int choice = readInt(scanner);

            switch (choice) {
                case 1:
                    System.out.print("Enter ID (integer): ");
                    int id = readInt(scanner);
                    System.out.print("Enter Name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter Branch: ");
                    String branch = scanner.nextLine();
                    System.out.print("Enter Year (integer): ");
                    int year = readInt(scanner);
                    System.out.print("Enter Marks (numeric): ");
                    double marks = readDouble(scanner);
                    Student s = new Student(id, name, branch, year, marks);
                    if (manager.addStudent(s)) {
                        System.out.println("Student added successfully.");
                    } else {
                        System.out.println("ID already exists. Try another.");
                    }
                    break;

                case 2:
                    System.out.println("\n--- All Students ---");
                    for (Student stu : manager.getAllStudents()) {
                        System.out.println(stu);
                    }
                    break;

                case 3:
                    System.out.print("Enter ID to update: ");
                    int upId = readInt(scanner);
                    Student toUpdate = manager.getStudentById(upId);
                    if (toUpdate != null) {
                        System.out.print("Enter New Name: ");
                        name = scanner.nextLine();
                        System.out.print("Enter New Branch: ");
                        branch = scanner.nextLine();
                        System.out.print("Enter New Year: ");
                        year = readInt(scanner);
                        System.out.print("Enter New Marks: ");
                        marks = readDouble(scanner);
                        manager.updateStudent(upId, name, branch, year, marks);
                        System.out.println("Student updated.");
                    } else {
                        System.out.println("Student not found.");
                    }
                    break;

                case 4:
                    System.out.print("Enter ID to delete: ");
                    int delId = readInt(scanner);
                    if (manager.deleteStudent(delId)) {
                        System.out.println("Student deleted.");
                    } else {
                        System.out.println("Student not found.");
                    }
                    break;

                case 5:
                    System.out.print("Enter name or part of name: ");
                    String part = scanner.nextLine();
                    List<Student> found = manager.searchByName(part);
                    if (found.isEmpty()) {
                        System.out.println("No students found.");
                    } else {
                        for (Student stu : found) {
                            System.out.println(stu);
                        }
                    }
                    break;

                case 6:
                    Optional<Student> top = manager.getTopScorer();
                    System.out.println("--- Statistics ---");
                    if (top.isPresent()) {
                        System.out.println("Top Scorer: " + top.get());
                    } else {
                        System.out.println("No records to evaluate.");
                    }
                    System.out.printf("Average Marks: %.2f\n", manager.getAverageMarks());
                    break;

                case 7:
                    System.out.println("Exiting... Thank you!");
                    return;

                default:
                    System.out.println("Invalid choice. Try again.");
            }
        }
    }

    private static int readInt(Scanner scanner) {
        while (true) {
            try {
                int val = scanner.nextInt();
                scanner.nextLine(); // clear newline
                return val;
            } catch (InputMismatchException e) {
                System.out.print("Invalid input. Please enter an integer: ");
                scanner.nextLine();
            }
        }
    }

    private static double readDouble(Scanner scanner) {
        while (true) {
            try {
                double val = scanner.nextDouble();
                scanner.nextLine(); // clear newline
                return val;
            } catch (InputMismatchException e) {
                System.out.print("Invalid input. Please enter a number: ");
                scanner.nextLine();
            }
        }
    }
}
