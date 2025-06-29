import java.util.*;
import java.io.*;
import org.json.JSONArray;
import org.json.JSONObject;

public class StudentManager {
	private List<Student> students;
	private final String FILE_NAME = "students.json";
	
	public StudentManager() {
		students = new ArrayList<>();
		loadFromFile();
	}
	
	public void addStudent(Student student) {
		for (Student s : students) {
			if(s.getStudentId().equals(student.getStudentId())) {
				System.out.println("ID already exists!");
				return;
			}
		}
		students.add(student);
		saveToFile();
	}
	
	public void viewStudents() {
		if(students.isEmpty()) {
			System.out.println("No Students found.");
			return;
		}
		students.forEach(System.out::println);
	}
	
	public void updateStudent(String id, Scanner sc) {
		for(Student s:students) {
			if(s.getStudentId().equals(id)) {
				System.out.println("New Name: ");
				s.setName(sc.nextLine());;
				System.out.println("New Branch: ");
				s.setBranch(sc.nextLine());
				System.out.println("New Year: ");
				s.setYear(Integer.parseInt(sc.nextLine()));
				System.out.println("New Marks: ");
				s.setMarks(Double.parseDouble(sc.nextLine()));;
				saveToFile();
				return;
			}
		}
		System.out.println("Student not found.");
	}
	
	public void deleteStudent(String id) {
		students.removeIf(s -> s.getStudentId().equals(id));
		saveToFile();
	}
	
	public void searchById(String id) {
		students.stream()
			.filter(s -> s.getStudentId().equals(id))
			.forEach(System.out::println);
	}
	
	public void searchByName(String name) {
		students.stream()
			.filter(s -> s.getName().equalsIgnoreCase(name))
			.forEach(System.out::println);
	}
	
	public void showStatistics() {
		if(students.isEmpty()) {
			System.out.println("No data to analyze.");
			return;
		}
		double totalMarks = 0;
		Student topScorer = students.get(0);
		for(Student s : students) {
			totalMarks += s.getMarks();
			if(s.getMarks() > topScorer.getMarks()) {
				topScorer = s;
			}
		}
		double avg = totalMarks / students.size();
		
		System.out.println("Average Marks: " + avg);
		System.out.println("Top Scorer: " + topScorer.getName() + " with " + topScorer.getMarks());
	}
	
	private void saveToFile() {
		JSONArray arr = new JSONArray();
		for(Student s: students) {
			arr.put(s.toJSON());
		}
		
		try(FileWriter writer = new FileWriter(FILE_NAME)){
			writer.write(arr.toString(4));
		}catch(IOException e) {
			System.out.println("Error saving data.");
		}
	}
	
	private void loadFromFile() {
		File file = new File(FILE_NAME);
		if(!file.exists()) return;
		
		try {
			String content = new String(java.nio.file.Files.readAllBytes(file.toPath()));
			JSONArray arr = new JSONArray(content);
			for(int i=0; i<arr.length(); i++) {
				students.add(Student.formJSON(arr.getJSONObject(i)));
			}
		}catch(Exception e) {
			System.out.println("Error loading data.");
		}
	}
}
