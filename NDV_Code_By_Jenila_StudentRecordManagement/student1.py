import json
import os

DATA_FILE = "students.json"

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


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.students = json.load(f)
        else:
            self.students = []

    def save_students(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No records found.")
            return
        print("\n Student Records:")
        print("{:<10} {:<20} {:<10} {:<6} {:<6}".format("ID", "Name", "Branch", "Year", "Marks"))
        for s in self.students:
            print("{:<10} {:<20} {:<10} {:<6} {:<6}".format(
                s["student_id"], s["name"], s["branch"], s["year"], s["marks"]
            ))

    def update_student(self, student_id):
        for s in self.students:
            if s["student_id"] == student_id:
                s["name"] = input("Enter new name: ")
                s["branch"] = input("Enter new branch: ")
                s["year"] = input("Enter new year: ")
                s["marks"] = input("Enter new marks: ")
                self.save_students()
                print(" Student updated successfully.")
                return
        print(" Student not found.")

    def delete_student(self, st_id):
        for s in self.students:
            if s["student_id"] == st1_id:
                self.students.remove(s)
                self.save_students()
                print(" Student deleted successfully.")
                return
        print(" Student not found.")

# Main menu loop
def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

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
            print("Exiting the program")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
