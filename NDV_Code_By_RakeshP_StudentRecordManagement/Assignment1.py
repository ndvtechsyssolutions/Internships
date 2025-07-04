import os
import json
class Students:

    def __init__(self,roll_no,name,branch,marks):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks
    def to_dict(self):
        return{
            "roll_no" : self.roll_no,
            "name" : self.name,
            "branch" : self.branch,
            "marks" : self.marks
        }
FILE_NAME = 'students.json'

def load_students():
    if not os.path.exists(FILE_NAME):
        return[]
    with open(FILE_NAME,'r') as file:
        return json.load(file)
def save_students(students):
    with open(FILE_NAME,'w') as file:
        return json.dump(students,file)
def add_students():
    roll_no = int(input("Enter Roll_number : "))
    name = input("Enter name : ")
    branch = input("Enter Branch : ")
    marks = float(input("Enter Marks : "))

    student = Students(roll_no,name,branch,marks)
    students = load_students()
    students.append(student.to_dict())
    save_students(students)
    print("Student data saved successfully")
def display_students() :
    students = load_students()
    if not students:
        print("No data Found")
    for det in students:
        print(f"Roll_num : {det['roll_no']}")
        print(f"Name : {det['name']}")
        print("Branch : ",det['branch'])
        print("Marks : ",det['marks'])
        print('-'*20)
def update_students():
    roll = int(input("Enter the student roll number to update the details : "))
    students = load_students()
    for det in students:
        if(roll == det['roll_no']):
            print("current details : \n")
            print(f"roll_no : {det['roll_no']}\n name : {det['name']} \n branch : {det['branch']} \n marks : {det['marks']}")
            det['roll_no'] = int(input("Enter the new Roll_no to update : "))
            det['name'] = input("Enter the new name to update : ")
            det['branch'] = input("Enter the new branch to update : ")
            det['marks'] = float(input("Enter the marks to update : "))
            save_students(students)
            print("Student details saved successfully")
        print("Students Roll Number not found")
def delete_students():
    roll = int(input("enter the Student Roll Number to delete : "))
    students = load_students()
    updated = [s for s in students if s['roll_no'] != roll]
    if len(students) == len(updated):
        print("Student not found")
    else:
        save_students(updated)
        print("Students deleted Successfully")

def menu():
    while True:
        print("1.Add Students")
        print("2.Display Students")
        print("3.Update Students")
        print("4.Delete Students")
        print("0.Exit")
        choice = int(input("Enter choice : "))
        if(choice == 1):
            add_students()
        elif(choice == 2):
            display_students()
        elif(choice == 3):
            update_students()
        elif(choice == 4):
            delete_students()
        elif(choice == 0):
            print("Exiting Program")
            break
        else :
            print("Invalid Choice")

if __name__ == "__main__":
    menu()
