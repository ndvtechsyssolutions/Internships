import org.json.JSONObject;

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
	
	public String getStudentId() {return studentId;}
	public String getName() {return name;}
	public String getBranch() {return branch;}
	public int getYear() {return year;}
	public double getMarks() {return marks;}
	
	public void setName(String name) {this.name = name;}
	public void setBranch(String branch) {this.branch = branch;}
	public void setYear(int year) {this.year = year;}
	public void setMarks(double marks) {this.marks = marks;}
	
	public JSONObject toJSON() {
		JSONObject obj = new JSONObject();
		obj.put("studentId", studentId);
		obj.put("name", name);
		obj.put("branch", branch);
		obj.put("year", year);
		obj.put("marks",marks);
		return obj;
	}
	public static Student formJSON(JSONObject obj) {
		return new Student(
				obj.getString("studentId"),
				obj.getString("name"),
				obj.getString("branch"),
				obj.getInt("year"),
				obj.getDouble("marks")
				);
	}
	
	@Override
	public String toString() {
		return studentId + " | " + name +" | "+branch+" | "+year+" | "+marks;
	}
	
}
