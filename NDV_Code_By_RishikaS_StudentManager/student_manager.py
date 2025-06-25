import json  # To read/write JSON files
from tabulate import tabulate  # Optional: for pretty tabular display

# File where student records will be stored
DATA_FILE = 'data.json'

# Define the Student class with required fields
class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    # Convert Student object to dictionary for easy storage in JSON
    def to_dict(self):
        return {
            "ID": self.student_id,
            "Name": self.name,
            "Branch": self.branch,
            "Year": self.year,
            "Marks": self.marks
        }

# Manager class to handle all operations like Add, View, Update, Delete
class StudentManager:
    def __init__(self):
        # Load existing data from file at startup
        self.students = self.load_data()

    # Load data from JSON file
    def load_data(self):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []  # Return empty list if file doesn't exist

    # Save current data to JSON file
    def save_data(self):
        with open(DATA_FILE, 'w') as file:
            json.dump(self.students, file, indent=4)

    # Add a new student record
    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        marks = input("Enter Marks: ")

        # Create a Student object and convert it to dictionary
        student = Student(student_id, name, branch, year, marks)
        self.students.append(student.to_dict())
        self.save_data()
        print("✅ Student added successfully!\n")

    # Display all student records in table format
    def view_students(self):
        if not self.students:
            print("⚠️ No student records found.")
        else:
            print("\n📋 Student Records:")
            print(tabulate(self.students, headers="keys", tablefmt="grid"))

    # Update a student record based on ID
    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student['ID'] == student_id:
                print("Leave field blank to keep existing value.")
                new_name = input(f"Enter new Name (current: {student['Name']}): ") or student['Name']
                new_branch = input(f"Enter new Branch (current: {student['Branch']}): ") or student['Branch']
                new_year = input(f"Enter new Year (current: {student['Year']}): ") or student['Year']
                new_marks = input(f"Enter new Marks (current: {student['Marks']}): ") or student['Marks']

                # Update values
                student['Name'] = new_name
                student['Branch'] = new_branch
                student['Year'] = new_year
                student['Marks'] = new_marks
                self.save_data()
                print("✅ Student updated successfully.")
                return
        print("❌ Student ID not found.")

    # Delete a student record based on ID
    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for student in self.students:
            if student['ID'] == student_id:
                self.students.remove(student)
                self.save_data()
                print("🗑️ Student deleted successfully.")
                return
        print("❌ Student ID not found.")

# Main function with menu-driven interface
def main():
    manager = StudentManager()
    while True:
        print("\n🎓 Student Record Management")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.update_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            print("👋 Exiting the program. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()
