import json
import os
from tabulate import tabulate

DATA_FILE = "students.json"

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
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    data = json.load(f)
                    self.students = [Student(**record) for record in data]
                except json.JSONDecodeError:
                    self.students = []
        else:
            self.students = []

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        marks = input("Enter Marks: ")
        student = Student(student_id, name, branch, year, marks)
        self.students.append(student)
        self.save_data()
        print("Student added successfully.\n")

    def view_students(self):
        if not self.students:
            print("No student records found.\n")
            return
        table = [s.to_dict() for s in self.students]
        print(tabulate(table, headers="keys", tablefmt="grid"))
        print()

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        for s in self.students:
            if s.student_id == student_id:
                print("Leave blank to keep current value.")
                name = input(f"Enter new Name [{s.name}]: ") or s.name
                branch = input(f"Enter new Branch [{s.branch}]: ") or s.branch
                year = input(f"Enter new Year [{s.year}]: ") or s.year
                marks = input(f"Enter new Marks [{s.marks}]: ") or s.marks
                s.name = name
                s.branch = branch
                s.year = year
                s.marks = marks
                self.save_data()
                print("Student record updated.\n")
                return
        print("Student ID not found.\n")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                self.save_data()
                print("Student record deleted.\n")
                return
        print("Student ID not found.\n")

def main():
    manager = StudentManager()
    while True:
        print("===== Student Record Management =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice (1-5): ")
        print()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
