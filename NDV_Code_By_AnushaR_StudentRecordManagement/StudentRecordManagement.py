import json
import os
from tabulate import tabulate

class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_dict(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Branch": self.branch,
            "Year": self.year,
            "Marks": self.marks
        }

class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully.\n")

    def view_students(self):
        if not self.students:
            print("No student records found.\n")
            return
        print("\nAll Student Records:")
        print(tabulate(self.students, headers="keys", tablefmt="grid"))

    def update_student(self, student_id):
        for student in self.students:
            if student["Student ID"] == student_id:
                print("Enter new details:")
                student["Name"] = input("Name: ")
                student["Branch"] = input("Branch: ")
                student["Year"] = input("Year: ")
                student["Marks"] = input("Marks: ")
                self.save_students()
                print("Student updated successfully.\n")
                return
        print("Student ID not found.\n")

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student["Student ID"] == student_id:
                del self.students[i]
                self.save_students()
                print("Student deleted successfully.\n")
                return
        print("Student ID not found.\n")

def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            student_id = input("Student ID: ")
            name = input("Name: ")
            branch = input("Branch: ")
            year = input("Year: ")
            marks = input("Marks: ")
            student = Student(student_id, name, branch, year, marks)
            manager.add_student(student)

        elif choice == '2':
            manager.view_students()

        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            manager.update_student(student_id)

        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            manager.delete_student(student_id)

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
