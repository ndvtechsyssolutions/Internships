from manager import StudentManager
from student import Student

def main():
    sm = StudentManager()

    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sid = input("ID: ")
            name = input("Name: ")
            branch = input("Branch: ")
            year = input("Year: ")
            marks = input("Marks: ")
            student = Student(sid, name, branch, year, marks)
            sm.add_student(student)

        elif choice == '2':
            sm.view_students()

        elif choice == '3':
            sid = input("Enter Student ID to update: ")
            if sm.update_student(sid):
                print("Student updated.")
            else:
                print("Student not found.")

        elif choice == '4':
            sid = input("Enter Student ID to delete: ")
            if sm.delete_student(sid):
                print("Student deleted.")
            else:
                print("Student not found.")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
