import json
from tabulate import tabulate

class Student:
    def _init_(self, sid, name, branch, year, marks):
        self.sid = sid
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

class Manager:
    def _init_(self, filename='students.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.students = json.load(f)
        except:
            self.students = []

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=2)

    def add_student(self, student):
        self.students.append(student._dict_)
        self.save_data()

    def view_students(self):
        print(tabulate(self.students, headers="keys", tablefmt="grid"))

    def update_student(self, sid, new_name):
        for s in self.students:
            if s["sid"] == sid:
                s["name"] = new_name
                self.save_data()
                print("Record updated.")
                return
        print("Student not found.")

    def delete_student(self, sid):
        self.students = [s for s in self.students if s["sid"] != sid]
        self.save_data()
        print("Record deleted.")

def main():
    m = Manager()
    while True:
        print("\n1. Add\n2. View\n3. Update\n4. Delete\n5. Exit")
        ch = input("Choose option: ")
        if ch == '1':
            s = Student(input("ID: "), input("Name: "), input("Branch: "), input("Year: "), input("Marks: "))
            m.add_student(s)
        elif ch == '2':
            m.view_students()
        elif ch == '3':
            m.update_student(input("ID to update: "), input("New Name: "))
        elif ch == '4':
            m.delete_student(input("ID to delete: "))
        elif ch == '5':
            break
        else:
            print("Invalid!")

main()
