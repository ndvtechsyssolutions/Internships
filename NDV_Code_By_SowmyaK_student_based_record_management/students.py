#.................STUDENT RECORD MANAGEMENT.........................

import json
import os

# Student class definition
class Student:
    def __init__(self, Stu_id, Name, Branch, Year, Marks):
        self.Stu_id = Stu_id
        self.Name = Name
        self.Branch = Branch
        self.Year = Year
        self.Marks = Marks

    def to_dict(self):
        return {
            "Stu_id": self.Stu_id,
            "Name": self.Name,
            "Branch": self.Branch,
            "Year": self.Year,
            "Marks": self.Marks
        }

    def display(self):
        print("Student_Reg.No:", self.Stu_id)
        print("Student_name:", self.Name)
        print("Student_branch:", self.Branch)
        print("Student_year:", self.Year)
        print("Student_obtained_marks:", self.Marks)


# Student Manager class definition
class Studentmanager:
    FILE_NAME = "student.json"

    def __init__(self):
        self.records = self.load_records()

    def load_records(self):
        if os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "r") as f:
                try:
                    data = json.load(f)
                    return [Student(**s) for s in data]
                except json.JSONDecodeError:
                    # File exists but is empty or corrupt
                    return []
        return []

    def save_students(self):
        with open(self.FILE_NAME, "w") as f:
            json.dump([s.to_dict() for s in self.records], f, indent=4)

    def add_student(self, student):
        self.records.append(student)
        self.save_students()
        print(".......Data Added Successfully.....")

    def view_students(self):
        if not self.records:
            print("No records found.")
        else:
            for s in self.records:
                s.display()

    def search_student(self, stu_id):
        for s in self.records:
            if s.Stu_id == stu_id:
                s.display()
                return
        print("Student not found.")

    def update_student(self, stu_id, new_name=None, new_branch=None, new_year=None, new_marks=None):
        for s in self.records:
            if s.Stu_id == stu_id:
                if new_name is not None:
                    s.Name = new_name
                if new_branch is not None:
                    s.Branch = new_branch
                if new_year is not None:
                    s.Year = new_year
                if new_marks is not None:
                    s.Marks = new_marks
                self.save_students()
                print("Student updated.")
                return
        print("Student not found.")

    def delete_student(self, stu_id):
        for s in self.records:
            if s.Stu_id == stu_id:
                self.records.remove(s)
                self.save_students()
                print("Student deleted.")
                return
        print("Student not found.")


# Main menu function
def main():
    manager = Studentmanager()

    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Stu_id = input("Enter Student ID: ")
            Name = input("Enter Name: ")
            Branch = input("Enter Branch: ")
            Year = input("Enter Year: ")
            Marks = float(input("Enter Marks: "))
            s = Student(Stu_id, Name, Branch, Year, Marks)
            manager.add_student(s)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            stu_id = input("Enter Student ID to search: ")
            manager.search_student(stu_id)

        elif choice == "4":
            stu_id = input("Enter Student ID to update: ")
            new_name = input("New Name (leave blank to keep): ")
            new_branch = input("New Branch (leave blank to keep): ")
            new_year = input("New Year (leave blank to keep): ")
            new_marks = input("New Marks (leave blank to keep): ")

            if new_name == "":
                new_name = None
            if new_branch == "":
                new_branch = None
            if new_year == "":
                new_year = None
            if new_marks == "":
                new_marks = None
            else:
                new_marks = float(new_marks)

            manager.update_student(stu_id, new_name, new_branch, new_year, new_marks)

        elif choice == "5":
            stu_id = input("Enter Student ID to delete: ")
            manager.delete_student(stu_id)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


# Entry point
if __name__ == "__main__":
    main()
