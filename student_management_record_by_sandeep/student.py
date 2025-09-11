
students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    students[roll] = {'Name': name, 'Age': age, 'Grade': grade}
    print("Student added successfully!\n")

def view_student():
    roll = input("Enter Roll Number to view: ")
    if roll in students:
        print("Student Details:")
        for key, value in students[roll].items():
            print(f"{key}: {value}")
    else:
        print("Student not found!\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        grade = input("Enter New Grade: ")
        students[roll] = {'Name': name, 'Age': age, 'Grade': grade}
        print("Student updated successfully!\n")
    else:
        print("Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")

def show_all_students():
    if students:
        print("All Student Records:")
        for roll, details in students.items():
            print(f"Roll: {roll}, Details: {details}")
    else:
        print("No records found.\n")

def menu():
    while True:
        print("\n---- Student Record Management ----")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Show All Students")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
