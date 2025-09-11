import json
import os

FILENAME = "students.json"

def load_data():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course Name: ")
    branch = input("Enter Branch Name: ")
    year = int(input("Enter Year of Study: "))
    marks = float(input("Enter Marks: "))
    student = {"roll": roll, "name": name, "course": course, "branch": branch, "year": year, "marks": marks}
    data.append(student)
    save_data(data)
    print("Student added successfully.")

def view_students():
    data = load_data()
    if not data:
        print("No records found.")
        return
    for s in data:
        print(f"Roll No: {s['roll']}, Name: {s['name']}, Course:{s['course']}, Branch: {s['branch']}, Year: {s['year']}, Marks: {s['marks']}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    data = load_data()
    found = False
    for s in data:
        if s['roll'] == roll:
            print(f"Found: Roll No: {s['roll']}, Name: {s['name']}, Course:{s['course']}, Branch: {s['branch']}, Year: {s['year']}, Marks: {s['marks']}")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    data = load_data()
    new_data = [s for s in data if s['roll'] != roll]
    if len(new_data) == len(data):
        print("Student not found.")
    else:
        save_data(new_data)
        print("Student deleted successfully.")

def update_student():
    roll = input("Enter Roll Number to update: ")
    data = load_data()
    for s in data:
        if s['roll'] == roll:
            s['name'] = input("Enter new name: ")
            s['course'] = input("Enter new course: ")
            s['branch'] = input("Enter new branch: ")
            s['year'] = int(input("Enter new year: "))
            s['marks'] = float(input("Enter new marks: "))
            save_data(data)
            print("Student updated successfully.")
            return
    print("Student not found.")

def main():
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
