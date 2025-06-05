import os
import pickle

# Define the Student class
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll}, Name: {self.name}, Marks: {self.marks}"

# File where records will be stored
FILE_NAME = "students.dat"

# Function to add a new student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    student = Student(roll, name, marks)

    with open(FILE_NAME, "ab") as file:
        pickle.dump(student, file)
    print("Student added successfully!")

# Function to display all students
def display_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    print("\n--- Student Records ---")
    with open(FILE_NAME, "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                print(student)
        except EOFError:
            pass

# Function to search for a student
def search_student():
    roll = input("Enter Roll No to search: ")
    found = False

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                if student.roll == roll:
                    print("Student found:\n", student)
                    found = True
                    break
        except EOFError:
            if not found:
                print("Student not found.")

# Function to delete a student
def delete_student():
    roll = input("Enter Roll No to delete: ")
    students = []
    found = False

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                if student.roll != roll:
                    students.append(student)
                else:
                    found = True
        except EOFError:
            pass

    with open(FILE_NAME, "wb") as file:
        for student in students:
            pickle.dump(student, file)

    print("Student deleted." if found else "Student not found.")

# Function to update a student's record
def update_student():
    roll = input("Enter Roll No to update: ")
    students = []
    found = False

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                if student.roll == roll:
                    print("Current Data:", student)
                    student.name = input("Enter new name: ")
                    student.marks = float(input("Enter new marks: "))
                    found = True
                students.append(student)
        except EOFError:
            pass

    with open(FILE_NAME, "wb") as file:
        for student in students:
            pickle.dump(student, file)

    print("Student updated." if found else "Student not found.")

# Main menu loop
def main():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
