import json
import os

class Student:
    def __init__(self, roll_no, name, course, marks):
        self.roll_no = roll_no
        self.name = name
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            'roll_no': self.roll_no,
            'name': self.name,
            'course': self.course,
            'marks': self.marks
        }

FILE_NAME = 'students.json'

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_students(students):
    with open(FILE_NAME, 'w') as file:
        json.dump(students, file, indent=4)

def add_student():
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))
    student = Student(roll_no, name, course, marks)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print("Student added successfully.")

def display_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"\nRoll No: {s['roll_no']}")
        print(f"Name: {s['name']}")
        print(f"Course: {s['course']}")
        print(f"Marks: {s['marks']}")
        print("-" * 30)

def search_student():
    roll = int(input("Enter Roll No to search: "))
    students = load_students()
    for s in students:
        if s['roll_no'] == roll:
            print(f"\nStudent Found:")
            print(f"Name: {s['name']}")
            print(f"Course: {s['course']}")
            print(f"Marks: {s['marks']}")
            return
    print("Student not found.")

def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    students = load_students()
    updated = [s for s in students if s['roll_no'] != roll]
    if len(students) == len(updated):
        print("Student not found.")
    else:
        save_students(updated)
        print("Student deleted successfully.")

def update_student():
    roll = int(input("Enter Roll No to update: "))
    students = load_students()
    for s in students:
        if s['roll_no'] == roll:
            print("Current details:")
            print(f"Name: {s['name']}, Course: {s['course']}, Marks: {s['marks']}")
            s['name'] = input("Enter new name: ")
            s['course'] = input("Enter new course: ")
            s['marks'] = float(input("Enter new marks: "))
            save_students(students)
            print("Student updated successfully.")
            return
    print("Student not found.")

# Menu
def menu():
    while True:
        print("\n- Student Record Management -")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    menu()
