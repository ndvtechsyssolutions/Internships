import os
import json

class Student:
    def __init__(self, roll, name, course, marks):
        self.roll = roll
        self.name = name
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "course": self.course,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data):
        # Backward compatibility (in case old keys like 'age' and 'grade' exist)
        course = data.get("course", data.get("age", "Unknown"))
        marks = data.get("marks", data.get("grade", "0"))
        return Student(data["roll"], data["name"], course, marks)


class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            try:
                data = json.load(f)
                return [Student.from_dict(d) for d in data]
            except json.JSONDecodeError:
                return []

    def save_students(self):
        with open(self.filename, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def add_student(self):
        roll = input("Enter Roll Number: ")
        if any(s.roll == roll for s in self.students):
            print("Student with this roll number already exists.")
            return
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = input("Enter Marks: ")
        student = Student(roll, name, course, marks)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
        print("\nAll Student Records:")
        for s in self.students:
            print(f"Roll: {s.roll}, Name: {s.name}, Course: {s.course}, Marks: {s.marks}")

    def search_student(self):
        roll = input("Enter Roll Number to search: ")
        for s in self.students:
            if s.roll == roll:
                print(f"Found: Roll: {s.roll}, Name: {s.name}, Course: {s.course}, Marks: {s.marks}")
                return
        print("Student not found.")

    def update_student(self):
        roll = input("Enter Roll Number to update: ")
        for s in self.students:
            if s.roll == roll:
                s.name = input("Enter new name: ")
                s.course = input("Enter new course: ")
                s.marks = input("Enter new marks: ")
                self.save_students()
                print("Student record updated.")
                return
        print("Student not found.")

    def delete_student(self):
        roll = input("Enter Roll Number to delete: ")
        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)
                self.save_students()
                print("Student record deleted.")
                return
        print("Student not found.")

    def menu(self):
        while True:
            print("\n===== Student Management System =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Try again!")


if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()
