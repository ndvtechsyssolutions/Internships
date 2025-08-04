import json
import os

# Define the file path for storing student data
DATA_FILE = 'students.json'

class Student:
    """
    Represents a single student record.
    """
    def __init__(self, student_id: str, name: str, branch: str, year: int, marks: float):
        """
        Initializes a new Student object.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Name of the student.
            branch (str): Branch of study.
            year (int): Academic year.
            marks (float): Marks obtained by the student.
        """
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_dict(self) -> dict:
        """
        Converts the Student object to a dictionary for JSON serialization.

        Returns:
            dict: A dictionary representation of the student.
        """
        return {
            "student_id": self.student_id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Creates a Student object from a dictionary.

        Args:
            data (dict): A dictionary containing student data.

        Returns:
            Student: A Student object.
        """
        return Student(
            data["student_id"],
            data["name"],
            data["branch"],
            data["year"],
            data["marks"]
        )

class StudentManager:
    """
    Manages the collection of student records, including loading, saving,
    adding, viewing, updating, and deleting.
    """
    def __init__(self, file_path: str):
        """
        Initializes the StudentManager.

        Args:
            file_path (str): The path to the JSON file for data persistence.
        """
        self.file_path = file_path
        self.students = self._load_data()

    def _load_data(self) -> list:
        """
        Loads student data from the JSON file.

        Returns:
            list: A list of Student objects.
        """
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Student.from_dict(item) for item in data]
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from file. Starting with empty records.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred while loading data: {e}")
            return []

    def _save_data(self):
        """
        Saves the current list of student records to the JSON file.
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([s.to_dict() for s in self.students], f, indent=4)
        except Exception as e:
            print(f"Error: Could not save data to file: {e}")

    def _find_student_by_id(self, student_id: str) -> Student | None:
        """
        Finds a student by their ID.

        Args:
            student_id (str): The ID of the student to find.

        Returns:
            Student | None: The Student object if found, otherwise None.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def add_student(self):
        """
        Prompts the user for student details and adds a new student record.
        Ensures student ID is unique.
        """
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ").strip()
        if not student_id:
            print("Student ID cannot be empty.")
            return

        if self._find_student_by_id(student_id):
            print(f"Error: Student with ID '{student_id}' already exists.")
            return

        name = input("Enter Name: ").strip()
        branch = input("Enter Branch: ").strip()

        while True:
            try:
                year = int(input("Enter Year: "))
                if year <= 0:
                    print("Year must be a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numerical year.")

        while True:
            try:
                marks = float(input("Enter Marks: "))
                if not (0 <= marks <= 100):
                    print("Marks must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numerical marks.")

        new_student = Student(student_id, name, branch, year, marks)
        self.students.append(new_student)
        self._save_data()
        print(f"Student '{name}' (ID: {student_id}) added successfully.")

    def view_students(self):
        """
        Displays all student records in a tabular format.
        """
        print("\n--- All Student Records ---")
        if not self.students:
            print("No student records available.")
            return

        # Define column headers
        headers = ["ID", "Name", "Branch", "Year", "Marks"]

        # Calculate maximum width for each column
        col_widths = {
            "ID": max(len(s.student_id) for s in self.students + [type('obj', (object,), {'student_id': headers[0]})()]),
            "Name": max(len(s.name) for s in self.students + [type('obj', (object,), {'name': headers[1]})()]),
            "Branch": max(len(s.branch) for s in self.students + [type('obj', (object,), {'branch': headers[2]})()]),
            "Year": max(len(str(s.year)) for s in self.students + [type('obj', (object,), {'year': headers[3]})()]),
            "Marks": max(len(str(s.marks)) for s in self.students + [type('obj', (object,), {'marks': headers[4]})()])
        }

        # Print header row
        header_line = (
            f"{headers[0]:<{col_widths['ID']}} | "
            f"{headers[1]:<{col_widths['Name']}} | "
            f"{headers[2]:<{col_widths['Branch']}} | "
            f"{headers[3]:<{col_widths['Year']}} | "
            f"{headers[4]:<{col_widths['Marks']}}"
        )
        print(header_line)
        print("-" * len(header_line))

        # Print each student record
        for student in self.students:
            print(
                f"{student.student_id:<{col_widths['ID']}} | "
                f"{student.name:<{col_widths['Name']}} | "
                f"{student.branch:<{col_widths['Branch']}} | "
                f"{student.year:<{col_widths['Year']}} | "
                f"{student.marks:<{col_widths['Marks']}.2f}"
            )
        print("-" * len(header_line))


    def update_student(self):
        """
        Prompts the user for a student ID and allows updating their details.
        """
        print("\n--- Update Student Record ---")
        student_id = input("Enter Student ID to update: ").strip()
        student = self._find_student_by_id(student_id)

        if not student:
            print(f"Error: Student with ID '{student_id}' not found.")
            return

        print(f"Found student: {student.name} (ID: {student.student_id})")
        print("Enter new details (leave blank to keep current value):")

        new_name = input(f"New Name ({student.name}): ").strip()
        if new_name:
            student.name = new_name

        new_branch = input(f"New Branch ({student.branch}): ").strip()
        if new_branch:
            student.branch = new_branch

        while True:
            new_year_str = input(f"New Year ({student.year}): ").strip()
            if not new_year_str:
                break
            try:
                new_year = int(new_year_str)
                if new_year <= 0:
                    print("Year must be a positive integer.")
                    continue
                student.year = new_year
                break
            except ValueError:
                print("Invalid input. Please enter a numerical year.")

        while True:
            new_marks_str = input(f"New Marks ({student.marks}): ").strip()
            if not new_marks_str:
                break
            try:
                new_marks = float(new_marks_str)
                if not (0 <= new_marks <= 100):
                    print("Marks must be between 0 and 100.")
                    continue
                student.marks = new_marks
                break
            except ValueError:
                print("Invalid input. Please enter numerical marks.")

        self._save_data()
        print(f"Student '{student.name}' (ID: {student.student_id}) updated successfully.")

    def delete_student(self):
        """
        Prompts the user for a student ID and deletes the corresponding record.
        """
        print("\nDelete Student Record:")
        student_id = input("Enter Student ID to delete: ").strip()
        initial_len = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]

        if len(self.students) < initial_len:
            self._save_data()
            print(f"Student with ID '{student_id}' deleted successfully.")
        else:
            print(f"Error: Student with ID '{student_id}' not found.")

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nStudent Record Management System:")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Update Student Record")
    print("4. Delete Student Record")
    print("5. Exit")
    print("----------------------------------------")

def main():
    """
    Main function to run the student record management console application.
    """
    manager = StudentManager(DATA_FILE)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            manager.update_student()
        elif choice == '4':
            manager.delete_student()
        elif choice == '5':
            print("Exiting Student Record Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()