#student record management system in console application
import json
import os
class Student:
    #create a constructor to initialize the student object
    def __init__(self, name,roll_no,course,marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            'name': self.name,
            'roll_no': self.roll_no,
            'course': self.course,
            'marks': self.marks
        }
    def display(self):
        print("Name is:",self.name)
        print("Roll No:",self.roll_no)
        print("Course is:",self.course) 
        print("Marks are:",self.marks)

class StudentManager:
    FILE_NAME = 'students.json'

    def load_students(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, 'r') as file:
                data = json.load(file)
                return [Student(**student) for student in data]
        return []
    
    #Save students to a file
    def save_students(self, students):
        with open(self.FILE_NAME, 'w') as file:
            json.dump([student.to_dict() for student in students], file, indent=4)
    #Add a student
    def add_student(self):
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))
        student = Student(name, roll_no, course, marks)
        students = self.load_students()
        students.append(student.to_dict())
        self.save_students(students)
        print("Student added successfully!")

    #Display all students
    def display_students(self):
        students = self.load_students()
        if not students:
            print("No students found.")
            return
        for student in students:
            s = Student(**student)
            s.display()
            print("-" * 20)

    #Search for a student by roll number
    def search_student(self):
        roll = int(input("Enter Roll No to search: "))
        students = self.load_students()
        for student in students:
            if student['roll_no'] == roll:
                s = Student(**student)
                s.display()
                return
        print("Student not found.")

    #Delete a student by roll number
    def delete_student(self):
        roll = int(input("Enter Roll No to delete: "))
        students = self.load_students()
        for student in students:
            if student['roll_no'] == roll:
                students.remove(student)
                self.save_students(students)
                print("Student deleted successfully!")
                return
        print("Student not found.")

    #Update a student's information
    def update_student(self):
        roll = int(input("Enter Roll No to update: "))
        students = self.load_students()
        for student in students:
            if student['roll_no'] == roll:
                name = input("Enter new Name (leave blank to keep current): ") or student['name']
                course = input("Enter new Course (leave blank to keep current): ") or student['course']
                marks = input("Enter new Marks (leave blank to keep current): ")
                if marks:
                    marks = float(marks)
                else:
                    marks = student['marks']
                updated_student = Student(name, roll, course, marks)
                students[students.index(student)] = updated_student.to_dict()
                self.save_students(students)
                print("Student updated successfully!")
                return
        print("Student not found.")

    #Display the menu
    def display_menu(self):
        while True:
            print("Student Record Management System")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Update Student")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.update_student()
            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

# Main function to run the application
if __name__ == "__main__":
    manager = StudentManager()
    manager.display_menu()
