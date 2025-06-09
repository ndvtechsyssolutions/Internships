import json
from student import Student
from tabulate import tabulate
import os

class StudentManager:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, student):
        self.students.append(student.to_dict())
        self.save_data()

    def view_students(self):
        if not self.students:
            print("No records found.")
        else:
            print(tabulate(self.students, headers="keys", tablefmt="grid"))

    def update_student(self, student_id):
        for student in self.students:
            if student["student_id"] == student_id:
                student["name"] = input("New Name: ")
                student["branch"] = input("New Branch: ")
                student["year"] = input("New Year: ")
                student["marks"] = input("New Marks: ")
                self.save_data()
                return True
        return False

    def delete_student(self, student_id):
        initial_len = len(self.students)
        self.students = [s for s in self.students if s["student_id"] != student_id]
        self.save_data()
        return len(self.students) < initial_len
