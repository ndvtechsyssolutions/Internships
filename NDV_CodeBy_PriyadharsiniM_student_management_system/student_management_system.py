import json
import os

class Student:
    def __init__(self,roll_no,name,course,marks):
        self.roll_no=roll_no
        self.name=name
        self.course=course
        self.marks=marks

    def to_dict(self):
        return {
            'roll_no':self.roll_no,
            'name':self.name,
            'course':self.course,
            'marks':self.marks

        }
FILE_NAME ='students_json'

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,'r')as file:
        return json.load(file)
    
def save_students(students):
    with open(FILE_NAME,'w') as file:
        json.dump(students,file,indent=4)

def add_student():
    roll_no =int(input("Roll no is"))
    name = input("Name is")
    course = input("Course is")
    marks = int(input("Marks is"))

    student =Student(roll_no,name,course,marks)
    students=load_students()
    students.append(student.to_dict())

    save_students(students)
    print("student added successfully")

def display_student_record():
    students = load_students()
    if not students:
        print("Student record not found")
        return
    for s in students:
        print(f"\nRoll no:{s['roll_no']}" )
        print(f"\nname:{s['name']}" )
        print(f"\ncourse:{s['course']}" )
        print(f"\nmarks:{s['marks']}" )
        print("-"*30)

def search_student():
    roll =int(input("enter roll no"))
    student = load_students()
    for s in student:
        if s['roll_no']==roll:
            print(f"\nRoll no:{s['roll_no']}" )
            print(f"\nname:{s['name']}" )
            print(f"\ncourse:{s['course']}" )
            print(f"\nmarks:{s['marks']}" )
            print("-"*30)
            return
    print("Student not found")

def delete_student():
    roll = int(input("enter the roll no"))
    students = load_students()
    updated = [s for s in students if s['roll_no']!=roll]
    if(len(students)==len(updated)):
        print("Student not found")
    else:
        save_students(updated)
        print("Student deleted successfully")

def update_student():
    roll = int(input("enter the roll no to update"))
    students = load_students()
    for s in students:
        if s['roll_no']==roll:
            print("current details")
            print(f"Name: {s['name']},Course: {s['course']},Marks: {s['marks']}")
            s['name']= input("enter the name")
            s['course'] = input("enter the course")
            s['marks']= input("enter the marks")
            save_students(students)
            print("student updated successfully")
            return
    print("student not found")

def menu():
    while True:
        print("\n---Student record management")
        print("1.Add Student")
        print("2.Display all the student")
        print("3.Search student")
        print("4.Delete student")
        print("5.update student")
        print( "0. exit")

        choice = input("enter your choice")
        if choice=='1':
            add_student()
        elif choice=='2':
            display_student_record()
        elif choice=='3':
            search_student()
        elif choice=='4':
            delete_student()
        elif choice=='5':
            update_student()
        elif choice=='0':
            print("exiting program")
            break
        else:
            print("invalid choice! Try again")
def authenticate():
    password = input("Enter admin password: ")
    return password == "admin123"

if __name__ == '__main__':
    if authenticate():
        menu()
    else:
        print("Access Denied!")





        
