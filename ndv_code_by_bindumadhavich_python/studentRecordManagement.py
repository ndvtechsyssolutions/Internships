import json
import os

# ------------------- Student Class -------------------
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

# ------------------- Manager Class -------------------
class Manager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=4)

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        marks = input("Enter Marks: ")
        student = Student(student_id, name, branch, year, marks)
        self.students.append(student.to_dict())
        self.save_students()
        print("Student added successfully.\n")

    def view_students(self):
        if not self.students:
            print("No records found.\n")
            return

        print("{:<12} {:<20} {:<10} {:<6} {:<6}".format("Student ID", "Name", "Branch", "Year", "Marks"))
        print("-" * 60)
        for s in self.students:
            print("{:<12} {:<20} {:<10} {:<6} {:<6}".format(
                s['student_id'], s['name'], s['branch'], s['year'], s['marks']
            ))
        print()

    def update_student(self):
        student_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student['student_id'] == student_id:
                print("Leave blank to keep existing value.")
                name = input(f"Enter new Name [{student['name']}]: ") or student['name']
                branch = input(f"Enter new Branch [{student['branch']}]: ") or student['branch']
                year = input(f"Enter new Year [{student['year']}]: ") or student['year']
                marks = input(f"Enter new Marks [{student['marks']}]: ") or student['marks']
                student.update({'name': name, 'branch': branch, 'year': year, 'marks': marks})
                self.save_students()
                print("Student updated successfully.\n")
                return
        print("Student ID not found.\n")

    def delete_student(self):
        student_id = input("Enter Student ID to delete: ")
        for student in self.students:
            if student['student_id'] == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully.\n")
                return
        print("Student ID not found.\n")

# ------------------- Main Program -------------------
def main():
    manager = Manager()
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.update_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
