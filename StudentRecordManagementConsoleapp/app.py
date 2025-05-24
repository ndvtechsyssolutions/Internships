# student_record_manager.py
# Console-based Student Record Management System

students = []

# Function to add a new student
def add_student():
    print("\n--- Add New Student ---")
    roll = input("Enter Roll Number: ")
    # Check if roll already exists
    for student in students:
        if student['roll'] == roll:
            print("❌ Student with this roll number already exists!")
            return

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    cgpa = input("Enter CGPA: ")

    students.append({
        'roll': roll,
        'name': name,
        'branch': branch,
        'year': year,
        'cgpa': cgpa
    })
    print("✅ Student added successfully!")

# Function to display all students
def display_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No records to display.")
        return
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Branch: {student['branch']}, Year: {student['year']}, CGPA: {student['cgpa']}")

# Function to search for a student
def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"Found: {student}")
            return
    print("❌ Student not found.")

# Function to update a student record
def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student['roll'] == roll:
            print("Leave field blank to keep current value.")
            name = input(f"New Name ({student['name']}): ") or student['name']
            branch = input(f"New Branch ({student['branch']}): ") or student['branch']
            year = input(f"New Year ({student['year']}): ") or student['year']
            cgpa = input(f"New CGPA ({student['cgpa']}): ") or student['cgpa']

            student.update({'name': name, 'branch': branch, 'year': year, 'cgpa': cgpa})
            print("✅ Student record updated.")
            return
    print("❌ Student not found.")

# Function to delete a student
def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("✅ Student deleted.")
            return
    print("❌ Student not found.")

# Main menu
def main_menu():
    while True:
        print("\n======= Student Record Management =======")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("👋 Exiting Program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1 to 6.")

# Run the program
if __name__ == "__main__":
    main_menu()
