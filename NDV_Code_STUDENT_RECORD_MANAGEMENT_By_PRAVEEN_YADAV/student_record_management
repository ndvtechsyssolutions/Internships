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
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                self.students = [Student(**item) for item in data]

    def save_data(self):
        with open(DATA_FILE, 'w') as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        marks = float(input("Enter Marks: "))
        student = Student(student_id, name, branch, year, marks)
        self.students.append(student)
        self.save_data()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        table = [s.to_dict() for s in self.students]
        print(tabulate(table, headers="keys", tablefmt="grid"))

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter new Name: ")
                student.branch = input("Enter new Branch: ")
                student.year = input("Enter new Year: ")
                student.marks = float(input("Enter new Marks: "))
                self.save_data()
                print("Student updated successfully.")
                return
        print("Student not found.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_data()
                print("Student deleted successfully.")
                return
        print("Student not found.")

def main():
    manager = StudentManager()
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.update_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
