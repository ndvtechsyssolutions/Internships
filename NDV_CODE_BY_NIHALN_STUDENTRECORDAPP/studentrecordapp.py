import json
from tabulate import tabulate
import os

# File to store student records
DATA_FILE = "students.json"

# Student class
class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks
        }

# Manager class to handle operations
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                self.students = json.load(file)
        else:
            self.students = []

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.students, file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        for student in self.students:
            if student["student_id"] == student_id:
                print("❌ Student ID already exists!")
                return
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        marks = input("Enter Marks: ")

        new_student = Student(student_id, name, branch, year, marks)
        self.students.append(new_student.to_dict())
        self.save_data()
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No records found.")
            return
        print("\n--- Student Records ---")
        print(tabulate(self.students, headers="keys", tablefmt="fancy_grid"))

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student["student_id"] == student_id:
                print("Leave field blank to keep current value.")
                student["name"] = input(f"Name ({student['name']}): ") or student["name"]
                student["branch"] = input(f"Branch ({student['branch']}): ") or student["branch"]
                student["year"] = input(f"Year ({student['year']}): ") or student["year"]
                student["marks"] = input(f"Marks ({student['marks']}): ") or student["marks"]
                self.save_data()
                print("✅ Student updated.")
                return
        print("❌ Student ID not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for student in self.students:
            if student["student_id"] == student_id:
                self.students.remove(student)
                self.save_data()
                print("✅ Student deleted.")
                return
        print("❌ Student ID not found.")

# Main menu
def main():
    manager = StudentManager()
    while True:
        print("\n===== Student Record Management =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
