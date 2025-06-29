import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		StudentManager manager = new StudentManager();
		Scanner sc = new Scanner(System.in);
		int choice;
		
		do {
			System.out.println("\n--- Student Management Menu ---");
			System.out.println("1. Add Student");
			System.out.println("2. View Students");
			System.out.println("3. Update Student");
			System.out.println("4. Delete Student");
			System.out.println("5. Search by ID");
			System.out.println("6. Search by Name");
			System.out.println("7. View statistics");
			System.out.println("8. Exit");
			System.out.print("Choose option: ");
			choice = Integer.parseInt(sc.nextLine());
			
			switch(choice) {
			case 1:
				System.out.print("ID: ");
				String id = sc.nextLine();
				System.out.print("Name: ");
				String name = sc.nextLine();
				System.out.print("Branch: ");
				String branch = sc.nextLine();
				System.out.print("Year: ");
				int year = Integer.parseInt(sc.nextLine());
				System.out.print("Marks: ");
				double marks = Double.parseDouble(sc.nextLine());
				
				Student s = new Student(id, name, branch, year, marks);
				manager.addStudent(s);
				break;
			case 2:
				manager.viewStudents();
				break;
			case 3:
				System.out.print("Enter ID to update: ");
				manager.updateStudent(sc.nextLine(), sc);
				break;
			case 4:
				System.out.print("Enter ID to delete: ");
				manager.deleteStudent(sc.nextLine());
				break;
			case 5:
				System.out.print("Enter ID to search: ");
				manager.searchById(sc.nextLine());
				break;
			case 6:
				System.out.print("Enter Name to search: ");
				manager.searchByName(sc.nextLine());
				break;
			case 7:
				manager.showStatistics();
				break;
			case 8:
				System.out.println("Exiting...");
				break;
			default:
				System.out.println("Invalid choice.");
		}
	}while(choice<=1 && choice>8);
	sc.close();
}
}