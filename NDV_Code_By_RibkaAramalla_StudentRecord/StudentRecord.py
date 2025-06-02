class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def to_dict(self):
        return {"ID": self.student_id, "Name": self.name, "Marks": self.marks}


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Add Student ---")
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        try:
            marks = float(input("Enter Marks: "))
            self.students.append(Student(student_id, name, marks))
            print("Student added successfully.")
        except ValueError:
            print("Invalid input. Marks must be a number.")

    def display_students(self):
        print("\n--- Student List ---")
        if not self.students:
            print("No student records found.")
        else:
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")

    def search_student(self):
        print("\n--- Search Student ---")
        search_id = input("Enter Student ID to search: ")
        for student in self.students:
            if student.student_id == search_id:
                print(f"Found: ID: {student.student_id}, Name: {student.name}, Marks: {student.marks}")
                return
        print("Student not found.")

    def update_student(self):
        print("\n--- Update Student ---")
        update_id = input("Enter Student ID to update: ")
        for student in self.students:
            if student.student_id == update_id:
                student.name = input("Enter new name: ")
                try:
                    student.marks = float(input("Enter new marks: "))
                    print("Record updated.")
                except ValueError:
                    print("Invalid marks. Update failed.")
                return
        print("Student not found.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        delete_id = input("Enter Student ID to delete: ")
        for i, student in enumerate(self.students):
            if student.student_id == delete_id:
                del self.students[i]
                print("Student deleted.")
                return
        print("Student not found.")

    def run(self):
        while True:
            print("\n===== Student Management Menu =====")
            print("1. Add Student")
            print("2. Display Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    app = StudentManagement()
    app.run()
