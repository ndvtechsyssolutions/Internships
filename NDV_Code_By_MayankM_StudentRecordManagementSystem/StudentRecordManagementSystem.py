 Description- Design and develop a Python console-based application that allows users to manage student records efficientlyusing OOP concepts and file handling and JSON for file persistence.

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

class Manager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_data()

    def view_students(self):
        if not self.students:
            print("No student records found.")
        else:
            print(tabulate(self.students, headers="keys", tablefmt="grid"))

    def update_student(self, student_id):
        for student in self.students:
            if student["Student ID"] == student_id:
                print("Found student. Enter new data:")
                student["Name"] = input("Name: ")
                student["Branch"] = input("Branch: ")
                student["Year"] = input("Year: ")
                student["Marks"] = input("Marks: ")
                self.save_data()
                print("Student record updated.")
                return
        print("Student ID not found.")

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student["Student ID"] == student_id:
                del self.students[i]
                self.save_data()
                print("Student record deleted.")
                return
        print("Student ID not found.")

def main():
    manager = Manager()

    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            sid = input("Student ID: ")
            name = input("Name: ")
            branch = input("Branch: ")
            year = input("Year: ")
            marks = input("Marks: ")
            student = Student(sid, name, branch, year, marks)
            manager.add_student(student)
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            sid = input("Enter Student ID to update: ")
            manager.update_student(sid)
        elif choice == '4':
            sid = input("Enter Student ID to delete: ")
            manager.delete_student(sid)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

OUTPUT:-
--- Student Record Management ---
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 1
Student ID: 101
Name: Mayank Sarkar
Branch: CSE
Year: 2
Marks: 89
