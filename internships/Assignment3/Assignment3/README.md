Overview
This is a Java-based Student Management System for Assignment 3. It enables users to manage student records, including adding, viewing, and updating student information.
Structure

StudentManagementSystem.java: Main class containing the program logic and main method to run the application.
student.java: Class defining the Student object with attributes (e.g., name, ID, grades) and related methods.
README.md: This documentation file.

How to Run

Prerequisites:

Java Development Kit (JDK) 8 or higher installed.
A Java IDE (e.g., IntelliJ IDEA, Eclipse) or command-line tools.


Steps:

Clone the repository: git clone <repository-url>
Navigate to the project folder: cd Assignment3
Compile the Java files:javac StudentManagementSystem.java student.java


Run the application:java StudentManagementSystem





Sample Inputs

Add a Student:
Input: Name: karthik, ID: 1001, Grade: 85
Output: Student karthik (ID: 1001) added successfully.


View Students:
Input: Select option to view all students.
Output: List of all students with their details.


Update Student:
Input: ID: 1001, New Grade: 90
Output: Student ID 1001 updated.



Notes

Ensure both Java files are in the same directory when compiling.
The program uses standard input (Scanner) for user interaction.
Basic error handling is included for invalid inputs.

