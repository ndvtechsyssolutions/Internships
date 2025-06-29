import json
import os
FILE_NAME = "studentsrecord.json"
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add a new student
def add_student():
    student = {
        "id": input("Enter student ID: "),
        "name": input("Enter name: "),
        "age": input("Enter age: "),
        "course": input("Enter course: "),
        "marks": input("Enter marks: ")
    }
    students = load_students()
    students.append(student)
    save_students(students)
    print("Student added successfully!")

# Display all students
def display_students():
    students = load_students()
    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}, Marks: {student['marks']}")

# Search for a student by ID
def search_student():
    id_to_find = input("Enter student ID to search: ")
    students = load_students()
    for student in students:
        if student['id'] == id_to_find:
            print(f" Found: {student}")
            return
    print("Student not found.")

# Delete a student by ID
def delete_student():
    id_to_delete = input("Enter student ID to delete: ")
    students = load_students()
    updated_students = [s for s in students if s['id'] != id_to_delete]
    if len(updated_students) == len(students):
        print("Student ID not found.")
    else:
        save_students(updated_students)
        print("Student deleted successfully.")

def main():
    while True:
        print("\nStudent Record Management")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
