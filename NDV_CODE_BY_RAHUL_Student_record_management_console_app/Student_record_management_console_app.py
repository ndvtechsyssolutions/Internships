import json
import os
from tabulate import tabulate  # For nicely formatted table display

class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    # Convert student object to dictionary (for JSON serialization)
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks
        }

    # Create a student object from a dictionary (for loading JSON)
    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["branch"],
            data["year"],
            data["marks"]
        )

# Class to manage multiple student records
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()  # Load existing records from file

    # Load student data from JSON file
    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as f:
            data = json.load(f)
            return {sid: Student.from_dict(info) for sid, info in data.items()}

    # Save student data to JSON file
    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({sid: student.to_dict() for sid, student in self.students.items()}, f, indent=4)
            print(f"Data saved to: {os.path.abspath(self.filename)}")

    # Add a new student record
    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Student already exists!")
            return
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        marks = input("Enter Marks: ")
        student = Student(student_id, name, branch, year, marks)
        self.students[student_id] = student
        self.save_data()
        print("Student added successfully.")

    # Display all student records in a tabular format
    def view_all_students(self):
        if not self.students:
            print("No records found.")
            return
        table = []
        for student in self.students.values():
            table.append([
                student.student_id,
                student.name,
                student.branch,
                student.year,
                student.marks
            ])
        headers = ["Student ID", "Name", "Branch", "Year", "Marks"]
        print("\n--- Student Records ---")
        print(tabulate(table, headers=headers, tablefmt="grid"))

    # Update an existing student record
    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        if student_id not in self.students:
            print("Student not found.")
            return
        name = input("Enter New Name: ")
        branch = input("Enter New Branch: ")
        year = input("Enter New Year: ")
        marks = input("Enter New Marks: ")
        self.students[student_id] = Student(student_id, name, branch, year, marks)
        self.save_data()
        print("Student record updated.")

    # Delete a student record
    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id not in self.students:
            print("Student not found.")
            return
        del self.students[student_id]
        self.save_data()
        print("Student deleted successfully.")

    # Display the menu and take user input
    def menu(self):
        while True:
            print("\n===== Student Record Management =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# Main execution block
if __name__ == "__main__":
    try:
        from tabulate import tabulate  # Ensure tabulate is available
    except ImportError:
        print("Installing 'tabulate' package...")
        import os
        os.system("pip install tabulate")  # Auto-install if missing

    manager = StudentManager()  # Create a manager instance
    manager.menu()  # Launch the menu interface




########################################################################

##json file

{
    "1": {
        "student_id": "1",
        "name": "hibro",
        "branch": "cse",
        "year": "2025",
        "marks": "100"
    },
    "2": {
        "student_id": "2",
        "name": "rahul",
        "branch": "cse",
        "year": "2025",
        "marks": "90"
    },
    "3": {
        "student_id": "3",
        "name": "satya",
        "branch": "aie",
        "year": "2025",
        "marks": "90"
    },
    "4": {
        "student_id": "4",
        "name": "dev",
        "branch": "eee",
        "year": "2025",
        "marks": "80"
    }
}
