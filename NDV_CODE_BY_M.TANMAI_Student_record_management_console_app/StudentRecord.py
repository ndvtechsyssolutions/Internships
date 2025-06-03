import os
import json

DATA_FILE = "students.json"

class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

class StudentManager:
    def __init__(self):
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    def save_students(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully.\n")

    def display_all_students(self):
        if not self.students:
            print("No student records found.\n")
            return
        for student in self.students:
            print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
        print()

    def search_student(self, roll_no):
        for student in self.students:
            if student["roll_no"] == roll_no:
                print(f"Found: Roll No: {student['roll_no']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}\n")
                return
        print("Student not found.\n")

    def delete_student(self, roll_no):
        for student in self.students:
            if student["roll_no"] == roll_no:
                self.students.remove(student)
                self.save_students()
                print("Student record deleted successfully.\n")
                return
        print("Student not found.\n")

    def update_student(self, roll_no):
        for student in self.students:
            if student["roll_no"] == roll_no:
                print("Enter new details:")
                student["name"] = input("New Name: ")
                student["age"] = input("New Age: ")
                student["course"] = input("New Course: ")
                self.save_students()
                print("Student record updated successfully.\n")
                return
        print("Student not found.\n")

def main():
    manager = StudentManager()

    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            roll_no = input("Enter Roll No: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")
            student = Student(roll_no, name, age, course)
            manager.add_student(student)

        elif choice == '2':
            manager.display_all_students()

        elif choice == '3':
            roll_no = input("Enter Roll No to search: ")
            manager.search_student(roll_no)

        elif choice == '4':
            roll_no = input("Enter Roll No to delete: ")
            manager.delete_student(roll_no)

        elif choice == '5':
            roll_no = input("Enter Roll No to update: ")
            manager.update_student(roll_no)

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
