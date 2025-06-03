import json
import os

class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,"name": self.name,"branch": self.branch,"year": self.year,"marks": self.marks
        }

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Branch: {self.branch}, Year: {self.year}, Marks: {self.marks}")

class StudentManager:

    FILE = "student.json"

    def load_data(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, 'r') as file:
                return json.load(file)
        return []
        
    def save_data(self, students):
        with open(self.FILE, 'w') as file:
                json.dump(students, file, indent=4)

    def add_student(self):
        students = self.load_data()
        student_id = input("Enter Student ID: ").strip()
        if any(s['student_id'].lower() == student_id.lower() for s in students):
            print("ID already exists.\n")
            return
        name = input("Enter Name: ").strip()
        branch = input("Enter Branch: ").strip()
        year = int(input("Enter Year (1-4): "))
        marks = int(input("Enter Marks (0-100): "))
        
        students.append(Student(student_id, name, branch, year, marks).to_dict())
        self.save_data(students)
        print("Student added.\n")

    def display_students(self):
        students = self.load_data()
        if not students:
            print("No students found.\n")
            return
        print("\nStudents:")
        for s in sorted(students, key=lambda x: x['name'].lower()):
            Student(s['student_id'], s['name'], s['branch'], s['year'], s['marks']).display()
        print()

    def update_student(self):
        students = self.load_data()
        sid = input("Enter ID to update: ").strip()
        for s in students:
            if s['student_id'].lower() == sid.lower():
                s['name'] = input(f"Name (current: {s['name']}): ").strip() or s['name']
                s['branch'] = input(f"Branch (current: {s['branch']}): ").strip() or s['branch']
                year = input(f"Year (current: {s['year']}): ").strip()
                marks = input(f"Marks (current: {s['marks']}): ").strip()
                s['year'] = int(year) if (year.isdigit() and 1 <= int(year) <= 4) else s['year']
                s['marks'] = int(marks) if (marks.isdigit() and 0 <= int(marks) <= 100) else s['marks']
                self.save_data(students)
                print("Student updated.\n")
                return
        print("Student not found.\n")

    def delete_student(self):
        students = self.load_data()
        sid = input("Enter ID to delete: ").strip()
        for s in students:
            if s['student_id'].lower() == sid.lower():
                students.remove(s)
                self.save_data(students)
                print("Student deleted.\n")
                return
        print("Student not found.\n")

def main():
    manager = StudentManager()
    while True:
        print("\n1. Add Student\n2. Display Students\n3. Update Student\n4. Delete Student\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == '1': 
            manager.add_student()
        elif choice == '2': 
            manager.display_students()
        elif choice == '3': 
            manager.update_student()
        elif choice == '4': 
            manager.delete_student()
        elif choice == '5': 
            print("Exiting.")
            break
        else: print("Invalid choice.\n")

if __name__ == "__main__":
    main()
