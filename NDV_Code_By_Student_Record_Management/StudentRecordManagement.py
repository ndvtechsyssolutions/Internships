import os
import json

# File to store student records
DATA_FILE = "students.json"

# Load existing student data from file
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save student data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Create a new student record
def add_student(data):
    student_id = input("Enter Student ID: ")
    if student_id in data:
        print("Student ID already exists.")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    data[student_id] = {"Name": name, "Age": age, "Course": course}
    print("Student record added successfully!")

# View all student records
def view_students(data):
    if not data:
        print("No student records found.")
        return
    print(f"{'ID':<10}{'Name':<20}{'Age':<5}{'Course':<15}")
    print("-" * 50)
    for student_id, details in data.items():
        print(f"{student_id:<10}{details['Name']:<20}{details['Age']:<5}{details['Course']:<15}")

# Update an existing student record
def update_student(data):
    student_id = input("Enter Student ID to update: ")
    if student_id not in data:
        print("Student ID not found.")
        return
    print(f"Current Details: {data[student_id]}")
    name = input("Enter New Name (leave blank to keep current): ") or data[student_id]["Name"]
    age = input("Enter New Age (leave blank to keep current): ") or data[student_id]["Age"]
    course = input("Enter New Course (leave blank to keep current): ") or data[student_id]["Course"]
    data[student_id] = {"Name": name, "Age": age, "Course": course}
    print("Student record updated successfully!")

# Delete a student record
def delete_student(data):
    student_id = input("Enter Student ID to delete: ")
    if student_id not in data:
        print("Student ID not found.")
        return
    del data[student_id]
    print("Student record deleted successfully!")

# Menu-driven program
def main():
    data = load_data()
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            update_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            save_data(data)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
