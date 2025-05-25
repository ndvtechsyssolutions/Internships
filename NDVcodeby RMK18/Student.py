import os
import json


class Student:
    def _init_(self, id, name, branch, year, marks):
        self.id=id
        self.name=name
        self.branch=branch
        self.year=year
        self.marks=marks
    
    def _str_(self):
        return f"ID: {self.id}, Name: {self.name}, Branch: {self.branch}, Year: {self.year}, Marks: {self.marks}"

    def to_dict(self):
        return {
            self.id:{
                "name": self.name,
                "branch": self.branch,
                "year": self.year,
                "marks": self.marks
            }
        }

class StudentManagement:
    def _init_(self):
        self.students= {}
        self.studentfile="students.json"
        self.load_students()

    def load_students(self):
        try:
            # Check if file exists
            if (not os.path.exists(self.studentfile)):
                with open(self.studentfile, 'w') as f:
                    json.dump({},f)
            # Load JSON data
            with open(self.studentfile, 'r') as f:
                data = json.load(f)
            # Convert back to Student objects
            self.students = {k: Student(k, v['name'], v['branch'], v['year'], v['marks']) for k, v in data.items()}
            # Store in self.students
            print(f"Loaded {len(self.students)} students from {self.studentfile}.")
            pass
        except FileNotFoundError:
            print(f"File {self.studentfile} not found. Initializing with an empty student list.")
            self.students = {}
            with open(self.studentfile, 'w') as f:
                json.dump({}, f)
            pass
        except json.JSONDecodeError:
            # Handle JSON decode error
            print(f"Error decoding JSON from {self.studentfile}. Initializing with an empty student list.")
            self.students = {}  
            with open(self.studentfile, 'w') as f:
                json.dump({}, f)
            pass

    def save_students(self):
        try:
            # Convert all students to a dictionary format
            if not self.students:
                print("No students to save.")
                return
            all_students = {student_id: {"name": student.name,"branch": student.branch,"year": student.year,"marks": student.marks} for student_id, student in self.students.items()}
            # Save to JSON file
            with open(self.studentfile, 'w') as f:
                json.dump(all_students, f, indent=4)
            pass
        except Exception as e:
            print(f"Error saving students: {e}")

    def add_student(self):
        try:
            # Get input from user
            student_id = input("Enter Student ID: ").strip()
            
            # Check if ID already exists
            if student_id in self.students:
                print("Student ID already exists!")
                return
                
            # Get other details
            name = input("Enter Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return
            branch = input("Enter Branch: ").strip()
            try:
                year = int(input("Enter Year: ").strip())
                if 1 <= year <= 4:
                    pass
                else:
                    print("Year must be between 1 and 4.")
                    return
            except ValueError:
                print("Invalid input for Year. Please enter a number between 1 and 4.")
                return

            try:     
                marks = float(input("Enter Marks: ").strip())
                if 0 <= marks <= 100:
                    pass
                else: 
                    print("Marks must be between 0 and 100.")
                    return
            except ValueError:
                print("Invalid input for Marks. Please enter a number between 0 and 100.")
                return
            
            # Create student object
            new_student = Student(student_id, name, branch, year, marks)
            # Add to self.students
            self.students[student_id] = new_student
            print(f"Student {name} added successfully.")
            # Save to file
            self.save_students()
            
        except Exception as e:
            print(f"Error adding student: {e}")

    def view_all_students(self):
        if not self.students:
            print("No students found!")
            return
        
        # Print in tabular format
        print("_"*60)
        print(f"{'ID':<15} {'Name':<20} {'Branch':<10} {'Year':<10} {'Marks':<10}")
        print("_"*60)
        for student in self.students.values():
            print(f"{student.id:<15} {student.name:<20} {student.branch:<10} {student.year:<10} {student.marks:<10}")
        print("_"*60)

    def update_student(self):
        # Ask for student ID
        student_id = input("Enter Student ID to update: ").strip()
        # Check if exists
        if student_id not in self.students:
            print("Student ID not found!")
            return
        # Show current details
        print("Current details:")
        print(self.students[student_id])
        # Ask what to update
        print("What do you want to update?")
        print("1. Name")
        print("2. Branch")
        print("3. Year")
        print("4. Marks")
        choice = input("Enter your choice (1-4): ").strip()
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice!")
            return
        # Get new value
        if choice == '1':
            new_value = input("Enter new Name: ").strip()
            if not new_value:
                print("Name cannot be empty.")
                return
            self.students[student_id].name = new_value
        elif choice == '2':
            new_value = input("Enter new Branch: ").strip()
            self.students[student_id].branch = new_value
        elif choice == '3':
            try:
                new_value = int(input("Enter new Year (1-4): ").strip())
                if 1 <= new_value <= 4:
                    self.students[student_id].year = new_value
                else:
                    print("Year must be between 1 and 4.")
                    return
            except ValueError:
                print("Invalid input for Year. Please enter a number between 1 and 4.")
                return
        elif choice == '4':
            try:
                new_value = float(input("Enter new Marks (0-100): ").strip())
                if 0 <= new_value <= 100:
                    self.students[student_id].marks = new_value
                else:
                    print("Marks must be between 0 and 100.")
                    return
            except ValueError:
                print("Invalid input for Marks. Please enter a number between 0 and 100.")
                return
        # Update and save
        self.save_students()
        print(f"Student {student_id} updated successfully.")

    def delete_student(self):
        # Ask for student ID
        student_id = input("Enter the Student ID to delete: ").strip()
        # Check if exists
        if student_id not in self.students:
            print("Student ID not found!")
            return
        # Show current details
        print("Current details:")
        print(self.students[student_id])

        # Confirm deletion
        confirm = input("Are you sure you want to delete this student? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Deletion cancelled.")
            return
        # Remove from self.students
        del self.students[student_id]
        print(f"Student {student_id} deleted successfully.")
        # Remove and save
        self.save_students()

    def search_student(self):
        # Ask for student ID
        student_id = input("Enter Student ID to search: ").strip()
        # Display if found
        if student_id in self.students:
            print("Student found:")
            print(self.students[student_id])
        else:
            print("Student ID not found!")

    def display_menu(self):
        print("\n" + "="*50)
        print("STUDENT RECORD MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        print("="*50)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.search_student()
            elif choice == '6':
                print("Thank you for using Student Management System!")
                break
            else:
                print("Invalid choice! Please try again.")
            
            # Optional: pause before showing menu again
            input("\nPress Enter to continue...")

def main():
    # Create StudentManagement object
    sm = StudentManagement()
    # Call the run method
    sm.run()
    pass

if _name_ == "_main_":
    main()
