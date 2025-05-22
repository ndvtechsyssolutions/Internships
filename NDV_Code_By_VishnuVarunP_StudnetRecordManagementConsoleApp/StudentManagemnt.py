import os


class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_line(self):
        return f"{self.student_id},{self.name},{self.branch},{self.year},{self.marks}\n"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(",")
        return Student(*parts)

class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        students = []
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    students.append(Student.from_line(line))
        return students

    def save_students(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(student.to_line())

    def add_student(self):
        print("\n--- Add New Student ---")
        sid = input("ID: ")
        name = input("Name: ")
        branch = input("Branch: ")
        year = input("Year: ")
        marks = input("Marks: ")
        student = Student(sid, name, branch, year, marks)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!\n")

    def view_students(self):
        print("\n--- Student Records ---")
        if not self.students:
            print("No student records found.\n")
        else:
            print("ID\tName\tBranch\tYear\tMarks")
            for s in self.students:
                print(f"{s.student_id}\t{s.name}\t{s.branch}\t{s.year}\t{s.marks}")
            print()

    def update_student(self):
        print("\n--- Update Student ---")
        sid = input("Enter student ID to update: ")
        for s in self.students:
            if s.student_id == sid:
                s.name = input(f"New Name (current: {s.name}): ") or s.name
                s.branch = input(f"New Branch (current: {s.branch}): ") or s.branch
                s.year = input(f"New Year (current: {s.year}): ") or s.year
                s.marks = input(f"New Marks (current: {s.marks}): ") or s.marks
                self.save_students()
                print("Student updated successfully!\n")
                return
        print("Student ID not found.\n")

    def delete_student(self):
        print("\n--- Delete Student ---")
        sid = input("Enter student ID to delete: ")
        for s in self.students:
            if s.student_id == sid:
                self.students.remove(s)
                self.save_students()
                print("Student deleted successfully!\n")
                return
        print("Student ID not found.\n")


def main():
    manager = StudentManager()
    while True:
        print("===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
