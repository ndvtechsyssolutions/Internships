import os
import json

class Students:
    def __init__(self, roll_no, name, branch, marks):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "branch": self.branch,
            "marks": self.marks
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

def add_students():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks: "))

    student = Students(roll_no, name, branch, marks)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print("Student data saved successfully.")

def display_students():
    students = load_students()
    if not students:
        print("No data found.")
        return
    for det in students:
        print(f"Roll No: {det['roll_no']}")
        print(f"Name: {det['name']}")
        print(f"Branch: {det['branch']}")
        print(f"Marks: {det['marks']}")
        print('-' * 20)

def update_students():
    roll = int(input("Enter the Roll Number to update: "))
    students = load_students()
    found = False
    for det in students:
        if roll == det['roll_no']:
            found = True
            print("Current Details:")
            print(f"Roll No: {det['roll_no']}, Name: {det['name']}, Branch: {det['branch']}, Marks: {det['marks']}")
            det['roll_no'] = int(input("New Roll No: "))
            det['name'] = input("New Name: ")
            det['branch'] = input("New Branch: ")
            det['marks'] = float(input("New Marks: "))
            save_students(students)
            print("Student details updated successfully.")
            break
    if not found:
        print("Student not found.")

def delete_students():
    roll = int(input("Enter Roll Number to delete: "))
    students = load_students()
    updated = [s for s in students if s['roll_no'] != roll]
    if len(students) == len(updated):
        print("Student not found.")
    else:
        save_students(updated)
        print("Student deleted successfully.")

def menu():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("0. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_students()
        elif choice == 2:
            display_students()
        elif choice == 3:
            update_students()
        elif choice == 4:
            delete_students()
        elif choice == 0:
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
