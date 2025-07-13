import json
import os

class Student:
    def __init__(self, name, rollno, marks, course):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        self.course = course

    def to_dict(self):
        return {
            "name": self.name,
            "rollno": self.rollno,
            "marks": self.marks,
            "course": self.course
        }
    

FILE_NAME="students.json"

def load_students():
        if not os.path.exists(FILE_NAME):
            return[]
        with open(FILE_NAME,"r") as file:
            return json.load(file)
        
def save_students(students):
        with open(FILE_NAME,"w") as file:
            json.dump(students,file,indent=4)
            
def add_students():
    rollno = int(input("Enter the Roll No: "))
    name = input("Enter your Name: ")
    course = input("Enter your Course: ")
    marks = float(input("Enter your Marks: "))

    student_obj = Student(name, rollno, marks, course)
    student_list = load_students()
    student_list.append(student_obj.to_dict())
    save_students(student_list)
    print("Student added successfully.")
    
def display_students():
    students = load_students()
    if not students:  # This checks if the list is empty
        print("No students data found.")
        return
    for s in students:
        print(f"\nRoll no: {s['rollno']}")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Course: {s['course']}")
        print("-" * 30)

def search_students():
    roll = int(input("Enter roll no to search: "))  # Corrected this line
    students = load_students()
    for s in students:
        if s['rollno'] == roll:
            print("\nStudent found")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Course: {s['course']}")
            return
    print("Student not found")

def delete_students():
    try:
        roll = int(input("Enter the roll no to delete: ")) 
    except ValueError:
        print("Invalid roll number. Please enter a valid integer.")
        return
    
    students = load_students()
    updated = [s for s in students if s['rollno'] != roll]
    if len(students) == len(updated):
        print("Student not found.")
    else:
        save_students(updated)
        print("Student deleted successfully.")

def update_students():
        roll = int(input("enter roll no to update: "))
        students=load_students()
        for s in students:
            if s['rollno']== roll:
                print("current details")
                print("name: {s['name']},course:{s['course']} , marks:{s['marks']}")
                s['name']=input("enter new name")
                s['course']=input("enter the course")
                s['marks']=float(input("enter new marks:"))
                save_students(students)
                print("student updated successfully")
                return 
        print("students not found")

def menu():
        while True:
            print("\n ---students record management---")
            print("1. add students")
            print("2. display all students")
            print("3. search students")
            print("4. delete student")
            print("5. update students")
            print("0.exit")

            choice=int(input("enter your choice: "))

            if choice ==1:
                add_students()
            elif choice== 2:
                display_students()
            elif choice== 3:
                search_students()
            elif choice == 4:
                delete_students()
            elif choice == 5:
                update_students()
            elif choice == 0:
                print("exiting program")
                break
            else:
                print("invalid choice")
if __name__ == '__main__':
    menu()
