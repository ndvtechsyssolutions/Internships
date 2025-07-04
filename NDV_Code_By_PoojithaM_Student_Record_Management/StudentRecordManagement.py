import json
import os

class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

class StudentManager:
    def __init__(self, filename='students.json'):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.students = [Student(**student) for student in data]

    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump([vars(student) for student in self.students], file, indent=4)

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def view_students(self):
        if not self.students:
            print("No student records available.")
            return
        
        print("\n{:<10} {:<20} {:<15} {:<10} {:<10}".format(
            "ID", "Name", "Branch", "Year", "Marks"))
        print("-" * 65)
        for student in self.students:
            print("{:<10} {:<20} {:<15} {:<10} {:<10}".format(
                student.student_id, student.name, student.branch, 
                student.year, student.marks))

    def update_student(self, student_id, new_data):
        for student in self.students:
            if student.student_id == student_id:
                for key, value in new_data.items():
                    setattr(student, key, value)
                self.save_students()
                return True
        return False

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                self.save_students()
                return True
        return False

def main():
    manager = StudentManager()
    
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("\nAdd New Student")
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            year = input("Enter Year: ")
            marks = input("Enter Marks: ")
            
            student = Student(student_id, name, branch, year, marks)
            manager.add_student(student)
            print("Student added successfully!")
            
        elif choice == '2':
            print("\nStudent Records")
            manager.view_students()
            
        elif choice == '3':
            print("\nUpdate Student")
            student_id = input("Enter Student ID to update: ")
            print("Leave blank to keep current value")
            name = input(f"Enter new Name: ")
            branch = input(f"Enter new Branch: ")
            year = input(f"Enter new Year: ")
            marks = input(f"Enter new Marks: ")
            
            new_data = {}
            if name: new_data['name'] = name
            if branch: new_data['branch'] = branch
            if year: new_data['year'] = year
            if marks: new_data['marks'] = marks
            
            if manager.update_student(student_id, new_data):
                print("Student updated successfully!")
            else:
                print("Student not found!")
                
        elif choice == '4':
            print("\nDelete Student")
            student_id = input("Enter Student ID to delete: ")
            if manager.delete_student(student_id):
                print("Student deleted successfully!")
            else:
                print("Student not found!")
                
        elif choice == '5':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
