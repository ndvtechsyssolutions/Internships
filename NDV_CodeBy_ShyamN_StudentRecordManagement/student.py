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
        return self.__dict__

class StudentApp:
    def __init__(self):
        self.students = self.load_data()

    def load_data(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                return [Student(**d) for d in data]
        return []

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([s.to_dict() for s in self.students], f, indent=2)

    def add(self):
        sid = input("ID: ")
        name = input("Name: ")
        branch = input("Branch: ")
        year = input("Year: ")
        marks = input("Marks: ")
        self.students.append(Student(sid, name, branch, year, marks))
        self.save_data()
        print("Student added.\n")

    def view(self):
        if not self.students:
            print("No records.\n")
            return
        for s in self.students:
            print(f"{s.student_id} | {s.name} | {s.branch} | {s.year} | {s.marks}")
        print()

    def update(self):
        sid = input("Enter ID to update: ")
        for s in self.students:
            if s.student_id == sid:
                s.name = input("New Name: ") or s.name
                s.branch = input("New Branch: ") or s.branch
                s.year = input("New Year: ") or s.year
                s.marks = input("New Marks: ") or s.marks
                self.save_data()
                print("Updated.\n")
                return
        print("Student not found.\n")

    def delete(self):
        sid = input("Enter ID to delete: ")
        self.students = [s for s in self.students if s.student_id != sid]
        self.save_data()
        print("Deleted (if existed).\n")

    def menu(self):
        while True:
            print("1. Add\n2. View\n3. Update\n4. Delete\n5. Exit")
            choice = input("Choose: ")
            if choice == '1': self.add()
            elif choice == '2': self.view()
            elif choice == '3': self.update()
            elif choice == '4': self.delete()
            elif choice == '5': break
            else: print("Invalid choice.\n")

if __name__ == "__main__":
    app = StudentApp()
    app.menu()
