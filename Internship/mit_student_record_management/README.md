# Student Record Management Console App
This is a console-based application built with Python for managing student records. It allows you to add, view, update and delete student information where the data is stored in a JSON file.

How to run the program:

1: Open your terminal or command prompt.

2: Navigate to the student_app directory:

```
cd ~/student_app
```

(Replace ~ with the actual path to where you stored the project)

3: Execute the main.py file:
```
python main.py
```

The application's menu will be displayed.

---

## Sample Inputs and Outputs

```
python main.py
```

Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 1

--- Add New Student ---

Enter Student ID: 105  

Enter Name: Jakob Hall

Enter Branch: Finance

Enter Year: 2023

Enter Marks: 87

Student 'Jakob Hall' (ID: 105) added successfully.

Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 2

--- All Student Records ---

ID  | Name       | Branch  | Year | Marks

-----------------------------------------

101 | John Doe   | CS      | 2025 | 70.00

102 | Jane Doe   | HR      | 2025 | 80.00

105 | Jakob Hall | Finance | 2023 | 87.00

-----------------------------------------

Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 3

--- Update Student Record ---

Enter Student ID to update: 105

Found student: Jakob Hall (ID: 105)

Enter new details (leave blank to keep current value):

New Name (Jakob Hall):

New Branch (Finance): 

New Year (2023): 2024

New Marks (87.0): 80

Student 'Jakob Hall' (ID: 105) updated successfully.


Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 2

--- All Student Records ---

ID  | Name       | Branch  | Year | Marks

-----------------------------------------

101 | John Doe   | CS      | 2025 | 70.00

102 | Jane Doe   | HR      | 2025 | 80.00

105 | Jakob Hall | Finance | 2024 | 80.00

-----------------------------------------


Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 4

Delete Student Record:

Enter Student ID to delete: 105

Student with ID '105' deleted successfully.

Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 2

--- All Student Records ---

ID  | Name     | Branch | Year | Marks

--------------------------------------

101 | John Doe | CS     | 2025 | 70.00

102 | Jane Doe | HR     | 2025 | 80.00

--------------------------------------


Student Record Management System:
1. Add New Student
2. View All Students
3. Update Student Record
4. Delete Student Record
5. Exit
----------------------------------------
Enter your choice (1-5): 5

Exiting Student Record Management System.