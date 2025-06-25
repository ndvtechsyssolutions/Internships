🎓 Student Record Management Console App

📖 Overview

This is a Python console-based application that helps you manage student records using Object-Oriented Programming (OOP) and JSON file handling It is menu-driven and allows the user to perform the following operations:

✅ Add a new student
📋 View all student records
📝 Update student details
🗑️ Delete a student
💾 Persist data using a data.json file
🛠️ Technologies Used

Python 3.x
JSON for data storage
tabulate (for formatted table display)
📦 Installation

Clone this repository or download the script files.

Install required dependencies:

pip install tabulate

Run the app:

python student_manager.py

📂 File Structure

student_management/
├── student_manager.py # Main Python script
├── data.json # Auto-created JSON file storing student data
└── README.md # Project documentation

🔑 Features

Add Student: Input new student data and store it in the file.

View Students: Display all records in a well-formatted table.

Update Student: Modify existing student information using the ID.

Delete Student: Remove a student from the system by ID.

Persistent Storage: All records are saved in data.json.

📘 Notes
If data.json does not exist, it will be created automatically.

The update option allows you to leave fields blank to retain existing values.

Data is always saved after any change (add, update, delete).

🧪 Sample Inputs and Outputs

🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 1
Enter Student ID: 1023
Enter Name: RAM
Enter Branch: CSE
Enter Year: 4
Enter Marks: 580
✅ Student added successfully!
🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 2
📋 Student Records:
+------+--------+----------+--------+---------+
| ID | Name | Branch | Year | Marks |
+======+========+==========+==+
| 1023 | RAM | CSE | 4 | 580 |
+------+--------+----------+--------+---------+

🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 3
Enter Student ID to update: 1023
Leave field blank to keep existing value.
Enter new Name (current: RAM):
Enter new Branch (current: CSE): ECE
Enter new Year (current: 4):
Enter new Marks (current: 580):
✅ Student updated successfully.
🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 1
Enter Student ID: 1065
Enter Name: PRIYA
Enter Branch: ISE
Enter Year: 3
Enter Marks: 560
✅ Student added successfully!
🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 2
📋 Student Records:
+------+--------+----------+--------+---------+
| ID | Name | Branch | Year | Marks |
+======+========+==========+==+
| 1023 | RAM | ECE | 4 | 580 |
+------+--------+----------+--------+---------+
| 1065 | PRIYA | ISE | 3 | 560 |
+------+--------+----------+--------+---------+

🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 4
Enter Student ID to delete: 1023
🗑️ Student deleted successfully.
🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 2
📋 Student Records:
+------+--------+----------+--------+---------+
| ID | Name | Branch | Year | Marks |
+======+========+==========+==+
| 1065 | PRIYA | ISE | 3 | 560 |
+------+--------+----------+--------+---------+

🎓 Student Record Management

Add Student
View All Students
Update Student
Delete Student
Exit
Enter your choice (1-5): 5
👋 Exiting the program. Goodbye!
