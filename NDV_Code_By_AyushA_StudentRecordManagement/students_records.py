import json
import os
from tabulate import tabulate
from datetime import datetime

class Student:
    """Class to represent a student record with all required fields"""
    def __init__(self, student_id: str, name: str, age: int, grade: str, 
                 email: str, phone: str, branch: str, year: int, marks: float):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.email = email
        self.phone = phone
        self.branch = branch
        self.year = year
        self.marks = marks
        self.enrollment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.last_updated = self.enrollment_date

    def to_dict(self) -> dict:
        """Convert student object to dictionary"""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'email': self.email,
            'phone': self.phone,
            'branch': self.branch,
            'year': self.year,
            'marks': self.marks,
            'enrollment_date': self.enrollment_date,
            'last_updated': self.last_updated
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create student object from dictionary"""
        return cls(
            data['student_id'],
            data['name'],
            data['age'],
            data['grade'],
            data['email'],
            data['phone'],
            data['branch'],
            data['year'],
            data['marks']
        )


class StudentManager:
    """Class to manage student records with file persistence"""
    def __init__(self, file_path: str = 'students.json'):
        self.file_path = file_path
        self.students = {}
        self.load_data()

    def load_data(self) -> None:
        """Load student data from JSON file"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    for student_id, student_data in data.items():
                        self.students[student_id] = Student.from_dict(student_data)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load student data ({str(e)}). Starting with empty database.")

    def save_data(self) -> None:
        """Save student data to JSON file"""
        data = {student_id: student.to_dict() 
               for student_id, student in self.students.items()}
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error: Could not save student data ({str(e)}).")

    def add_student(self, student: Student) -> bool:
        """Add a new student record"""
        if student.student_id in self.students:
            print(f"Error: Student ID {student.student_id} already exists.")
            return False
        self.students[student.student_id] = student
        self.save_data()
        return True

    def get_student(self, student_id: str) -> Student | None:
        """Get a student record by ID"""
        return self.students.get(student_id)

    def update_student(self, student_id: str, **kwargs) -> bool:
        """Update an existing student record"""
        student = self.get_student(student_id)
        if not student:
            print(f"Error: Student ID {student_id} not found.")
            return False
        
        for key, value in kwargs.items():
            if hasattr(student, key):
                setattr(student, key, value)
        
        student.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_data()
        return True

    def delete_student(self, student_id: str) -> bool:
        """Delete a student record"""
        if student_id not in self.students:
            print(f"Error: Student ID {student_id} not found.")
            return False
        
        del self.students[student_id]
        self.save_data()
        return True

    def get_all_students(self) -> list[Student]:
        """Get all student records"""
        return list(self.students.values())

    def display_students_table(self, detailed: bool = False) -> None:
        """Display all students in a tabular format"""
        if not self.students:
            print("No student records found.")
            return
        
        if detailed:
            headers = ["ID", "Name", "Age", "Grade", "Email", "Phone", "Branch", "Year", "Marks", "Enrolled", "Updated"]
            table_data = []
            
            for student in self.get_all_students():
                table_data.append([
                    student.student_id,
                    student.name,
                    student.age,
                    student.grade,
                    student.email,
                    student.phone,
                    student.branch,
                    student.year,
                    student.marks,
                    student.enrollment_date,
                    student.last_updated
                ])
        else:
            headers = ["Student ID", "Name", "Branch", "Year", "Grade", "Marks"]
            table_data = []
            
            for student in self.get_all_students():
                table_data.append([
                    student.student_id,
                    student.name,
                    student.branch,
                    student.year,
                    student.grade,
                    student.marks
                ])
        
        print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))


class StudentManagementApp:
    """Console application for student management"""
    def __init__(self):
        self.manager = StudentManager()
    
    def display_menu(self) -> None:
        """Display the main menu"""
        print("\n" + "=" * 50)
        print("Student Record Management System".center(50))
        print("=" * 50)
        print("1. Add Student")
        print("2. View Student Details")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students (Summary)")
        print("6. Display All Students (Detailed)")
        print("7. Exit")
        print("=" * 50)

    def get_valid_input(self, prompt: str, input_type=str, required=True, min_val=None, max_val=None) -> any:
        """Get validated user input with type checking and range validation"""
        while True:
            try:
                value = input(prompt).strip()
                if not value and required:
                    print("Error: This field is required.")
                    continue
                elif not value and not required:
                    return None
                
                if input_type == int:
                    value = int(value)
                    if min_val is not None and value < min_val:
                        print(f"Error: Value must be at least {min_val}.")
                        continue
                    if max_val is not None and value > max_val:
                        print(f"Error: Value must be at most {max_val}.")
                        continue
                elif input_type == float:
                    value = float(value)
                elif input_type == "email":
                    if '@' not in value or '.' not in value:
                        print("Error: Please enter a valid email address.")
                        continue
                
                return value
            except ValueError:
                print(f"Error: Please enter a valid {input_type.__name__ if input_type != 'email' else 'email'}.")

    def add_student_ui(self) -> None:
        """UI for adding a new student"""
        print("\n" + "=" * 50)
        print("Add New Student".center(50))
        print("=" * 50)
        
        student_id = self.get_valid_input("Enter Student ID: ")
        name = self.get_valid_input("Enter Name: ")
        age = self.get_valid_input("Enter Age: ", int, min_val=5, max_val=25)
        grade = self.get_valid_input("Enter Grade: ")
        email = self.get_valid_input("Enter Email: ", "email")
        phone = self.get_valid_input("Enter Phone: ")
        branch = self.get_valid_input("Enter Branch: ")
        year = self.get_valid_input("Enter Year: ", int, min_val=1, max_val=5)
        marks = self.get_valid_input("Enter Marks: ", float, min_val=0, max_val=100)
        
        student = Student(student_id, name, age, grade, email, phone, branch, year, marks)
        if self.manager.add_student(student):
            print(f"\nStudent {name} added successfully!")

    def view_student_ui(self) -> None:
        """UI for viewing a student's detailed information"""
        student_id = self.get_valid_input("\nEnter Student ID to view: ")
        student = self.manager.get_student(student_id)
        
        if student:
            print("\n" + "=" * 50)
            print("Student Details".center(50))
            print("=" * 50)
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
            print(f"Email: {student.email}")
            print(f"Phone: {student.phone}")
            print(f"Branch: {student.branch}")
            print(f"Year: {student.year}")
            print(f"Marks: {student.marks}")
            print(f"Enrollment Date: {student.enrollment_date}")
            print(f"Last Updated: {student.last_updated}")
            print("=" * 50)
        else:
            print(f"\nStudent with ID {student_id} not found.")

    def update_student_ui(self) -> None:
        """UI for updating a student record"""
        student_id = self.get_valid_input("\nEnter Student ID to update: ")
        student = self.manager.get_student(student_id)
        
        if not student:
            print(f"\nStudent with ID {student_id} not found.")
            return
        
        print("\nLeave blank to keep current value")
        update_data = {}
        
        name = input(f"Enter Name [{student.name}]: ").strip()
        if name: update_data['name'] = name
        
        age = input(f"Enter Age [{student.age}]: ").strip()
        if age: update_data['age'] = int(age)
        
        grade = input(f"Enter Grade [{student.grade}]: ").strip()
        if grade: update_data['grade'] = grade
        
        email = input(f"Enter Email [{student.email}]: ").strip()
        if email: update_data['email'] = email
        
        phone = input(f"Enter Phone [{student.phone}]: ").strip()
        if phone: update_data['phone'] = phone
        
        branch = input(f"Enter Branch [{student.branch}]: ").strip()
        if branch: update_data['branch'] = branch
        
        year = input(f"Enter Year [{student.year}]: ").strip()
        if year: update_data['year'] = int(year)
        
        marks = input(f"Enter Marks [{student.marks}]: ").strip()
        if marks: update_data['marks'] = float(marks)
        
        if update_data and self.manager.update_student(student_id, **update_data):
            print("\nStudent updated successfully!")
        else:
            print("\nNo changes made or update failed.")

    def delete_student_ui(self) -> None:
        """UI for deleting a student record"""
        student_id = self.get_valid_input("\nEnter Student ID to delete: ")
        if self.manager.delete_student(student_id):
            print("\nStudent deleted successfully!")

    def run(self) -> None:
        """Run the application"""
        while True:
            self.display_menu()
            choice = self.get_valid_input("\nEnter your choice (1-7): ", required=True)
            
            try:
                if choice == '1':
                    self.add_student_ui()
                elif choice == '2':
                    self.view_student_ui()
                elif choice == '3':
                    self.update_student_ui()
                elif choice == '4':
                    self.delete_student_ui()
                elif choice == '5':
                    self.manager.display_students_table(detailed=False)
                elif choice == '6':
                    self.manager.display_students_table(detailed=True)
                elif choice == '7':
                    print("\nExiting the application. Goodbye!")
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1-7.")
            except Exception as e:
                print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        app = StudentManagementApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted. Exiting gracefully...")
    except Exception as e:
        print(f"\nFatal error: {str(e)}")
