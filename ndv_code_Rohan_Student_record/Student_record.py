import json

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {"ID": self.student_id, "Name": self.name, "Marks": self.marks}

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))
        self.students.append(Student(student_id, name, marks))
        print("Student added successfully.")

    def display_students(self):
        if not self.students:
            print("No student records found.")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")

    def search_student(self):
        search_id = input("Enter Student ID to search: ")
        for student in self.students:
            if student.student_id == search_id:
                print(f"Found: ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")
                return
        print("Student not found.")

    def update_student(self):
        update_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student.student_id == update_id:
                student.name = input("Enter new name: ")
                student.marks = float(input("Enter new marks: "))
                print("Record updated.")
                return
        print("Student not found.")

    def delete_student(self):
        delete_id = input("Enter Student ID to delete: ")
        for i, student in enumerate(self.students):
            if student.student_id == delete_id:
                del self.students[i]
                print("Student deleted.")
                return
        print("Student not found.")

    def run(self):
        while True:
            print("\n1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

# Run the application
app = StudentManagement()
app.run()
