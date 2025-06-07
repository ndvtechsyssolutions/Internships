students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {'name': name, 'marks': marks}
    print("Student added.")

def view_student():
    roll = input("Enter Roll No to view: ")
    if roll in students:
        print(f"Name: {students[roll]['name']}, Marks: {students[roll]['marks']}")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        name = input("Enter new name: ")
        marks = input("Enter new marks: ")
        students[roll] = {'name': name, 'marks': marks}
        print("Student updated.")
    else:
        print("Student not found.")

def show_all():
    if students:
        for roll, data in students.items():
            print(f"Roll: {roll}, Name: {data['name']}, Marks: {data['marks']}")
    else:
        print("No records found.")

def main():
    while True:
        print("\n1. Add  2. View  3. Update  4. Delete  5. Show All  6. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            show_all()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option")

main()
