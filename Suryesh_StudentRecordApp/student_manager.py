# student_manager.py

import json
from student import Student

class StudentManager:
    def __init__(self):
        self.students = {}  # key: student_id, value: Student object

    def add_student(self, student):
        if student.student_id in self.students:
            print("❌ Student ID already exists!")
            return
        self.students[student.student_id] = student
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("📂 No student records found.")
            return
        for student in self.students.values():
            print(student)

    def update_student(self, student_id):
        if student_id not in self.students:
            print("❌ Student not found.")
            return

        student = self.students[student_id]
        print(f"🔁 Updating record for: {student.name}")
        student.name = input("Enter new name: ") or student.name
        student.branch = input("Enter new branch: ") or student.branch
        student.year = input("Enter new year: ") or student.year
        try:
            marks = input("Enter new marks: ")
            if marks:
                student.marks = float(marks)
        except ValueError:
            print("⚠️ Invalid marks input. Skipping update.")

        print("✅ Student updated successfully!")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("🗑️ Student deleted successfully!")
        else:
            print("❌ Student ID not found.")

    def search_by_id(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student)
        else:
            print("❌ Student not found.")

    def search_by_name(self, name):
        found = False
        for student in self.students.values():
            if student.name.lower() == name.lower():
                print(student)
                found = True
        if not found:
            print("❌ No student with that name found.")

    def top_scorer(self):
        if not self.students:
            print("⚠️ No student data available.")
            return
        top_student = max(self.students.values(), key=lambda s: s.marks)
        print("🏆 Top Scorer:")
        print(top_student)

    def average_marks(self):
        if not self.students:
            print("⚠️ No student data available.")
            return
        total = sum(s.marks for s in self.students.values())
        average = total / len(self.students)
        print(f"📊 Average Marks: {average:.2f}")

    def save_to_file(self, filename="students.json"):
        data = {sid: s.to_dict() for sid, s in self.students.items()}
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"💾 Data saved to {filename}")

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for student_id, record in data.items():
                    student = Student(**record)
                    self.students[student_id] = student
            print(f"📂 Data loaded from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found. Starting with empty records.")
        except json.JSONDecodeError:
            print("❌ Error decoding JSON. File may be corrupted.")
