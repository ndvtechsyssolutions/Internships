#student records management system
#json:-to store the records 
#classes and objects:-to reuse the data
#file system:-to create the record the data locally

import os
import json

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

FILE_NAME = 'students.json'

def load_student():
    if not os.path.exists(FILE_NAME):  
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_student(student):
    with open(FILE_NAME, 'w') as file:
        json.dump(student, file, indent=4)  

def add_student():
    student_id = int(input("Enter student ID: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    year = int(input("Enter year: "))
    marks = float(input("Enter Marks: "))
    student = Student(student_id, name, branch, year, marks)
    students = load_student()
    students.append(student.to_dict())
    save_student(students)
    print("Student added successfully")

def display_student():
    students = load_student()
    if not students:
        print("No student records found")
        return
    for s in students:
        print(f"\nStudent ID: {s['student_id']}")
        print(f"Name: {s['name']}")
        print(f"Branch: {s['branch']}")
        print(f"Year: {s['year']}")
        print(f"Marks: {s['marks']}")

def search_student():
    student_id = int(input("Enter student ID: "))
    students = load_student()  
    for s in students:
        if s['student_id'] == student_id:
            print(f"\nStudent Found:")
            print(f"Name: {s['name']}")
            print(f"Branch: {s['branch']}")
            print(f"Year: {s['year']}")
            print(f"Marks: {s['marks']}")
            return
    print("Student not found")  

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    students = load_student()
    updated = [s for s in students if s['student_id'] != student_id]
    if len(students) == len(updated):
        print("Student not found")
    else:
        save_student(updated)
        print("Student deleted successfully")

def update_student():
    student_id = int(input("Enter student ID to update: "))
    students = load_student()
    for s in students:
        if s['student_id'] == student_id:
            print("Current details:")
            print(f"Name: {s['name']}, Branch: {s['branch']}, Year: {s['year']}, Marks: {s['marks']}")
            s['name'] = input("Enter new name: ")
            s['branch'] = input("Enter new branch: ")
            s['year'] = int(input("Enter new year: "))
            s['marks'] = float(input("Enter new marks: "))
            save_student(students)
            print("Student updated successfully.")
            return
    print("Student not found.")

def menu():
    while True:
        print("\n1. Add student")
        print("2. Display all students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Update student")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_student()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '0':
            print("Exit")
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    menu()         
