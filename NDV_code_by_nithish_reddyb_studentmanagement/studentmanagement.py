import json
import os

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks
        }

    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["marks"]
        )

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, "r") as f:
            data = json.load(f)
            return {sid: Student.from_dict(info) for sid, info in data.items()}

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump({sid: student.to_dict() for sid, student in self.students.items()}, f, indent=4)
            print(f"Data saved to: {os.path.abspath(self.filename)}")

    def add_student(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            print("Student already exists!")
            return
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        student = Student(student_id, name, marks)
        self.students[student_id] = student
        self.save_data()
        print("Student added successfully.")

    def view_all_students(self):
        if not self.students:
            print("No records found.")
            return

        print("\n--- Student Records ---")
        print("{:<15} {:<20} {:<10}".format("Student ID", "Name", "Marks"))
        print("-" * 45)
        for student in self.students.values():
            print("{:<15} {:<20} {:<10}".format(
                student.student_id, student.name, student.marks))

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        if student_id not in self.students:
            print("Student not found.")
            return
        name = input("Enter New Name: ")
        marks = input("Enter New Marks: ")
        self.students[student_id] = Student(student_id, name, marks)
        self.save_data()
        print("Student record updated.")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        if student_id not in self.students:
            print("Student not found.")
            return
        del self.students[student_id]
        self.save_data()
        print("Student deleted successfully.")

    def menu(self):
        while True:
            print("\n===== Student Record Management =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    manager = StudentManager()
    manager.menu()




#json 

{
    "1": {
        "student_id": "1",
        "name": "nithish",
        "marks": "100"
    },
    "2": {
        "student_id": "2",
        "name": "gowri",
        "marks": "102"
    },
    "3": {
        "student_id": "3",
        "name": "pk",
        "marks": "90"
    },
    "5": {
        "student_id": "5",
        "name": "vid",
        "marks": "999"
    }
}
