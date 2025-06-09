# main.py

from student import Student
from student_manager import StudentManager

def get_student_input():
    student_id = input("Enter Student ID: ")
    if not student_id.isdigit():
        print("❌ Student ID must contain only numbers.")
        return None

    name = input("Enter Name: ")
    if not name.isalpha():
        print("❌ Name must contain only alphabets.")
        return None

    branch = input("Enter Branch: ")
    if not branch.isalnum():
        print("❌ Branch must be alphanumeric without special characters.")
        return None

    year = input("Enter Year: ")
    if not year.isdigit():
        print("❌ Year must contain only numbers.")
        return None

    marks_input = input("Enter Marks: ")
    if not marks_input.replace('.', '', 1).isdigit():
        print("❌ Marks must be a number.")
        return None

    marks = float(marks_input)
    return Student(student_id, name, branch, year, marks)

def main():
    manager = StudentManager()

    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search by ID")
        print("6. Search by Name")
        print("7. Top Scorer")
        print("8. Average Marks")
        print("9. Save to File")
        print("10. Load from File")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            student = get_student_input()
            if student:
                manager.add_student(student)
        elif choice == '2':
            manager.view_students()
        elif choice == '3':
            sid = input("Enter Student ID to update: ")
            manager.update_student(sid)
        elif choice == '4':
            sid = input("Enter Student ID to delete: ")
            manager.delete_student(sid)
        elif choice == '5':
            sid = input("Enter Student ID to search: ")
            manager.search_by_id(sid)
        elif choice == '6':
            name = input("Enter Name to search: ")
            manager.search_by_name(name)
        elif choice == '7':
            manager.top_scorer()
        elif choice == '8':
            manager.average_marks()
        elif choice == '9':
            manager.save_to_file()
        elif choice == '10':
            manager.load_from_file()
        elif choice == '11':
            print("👋 Exiting Student Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
