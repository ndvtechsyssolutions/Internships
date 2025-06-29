import json
import os

class Student:
    def __init__(self,roll_no,name,course,marks):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        self.marks=marks
    def to_dict(self):
        return{
            'roll_no':self.roll_no,
            'name':self.name,
            'course': self.course,
            'marks': self.marks
        }   
    
FILE_NAME='Student.json'

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,'r') as file:
        return json.load(file)
    
def save_data(students):
    with open(FILE_NAME,'w') as file:
        json.dump(students,file,indent=3)
    
def add_student():
    roll_no=int(input("\nEnter Student Roll No.: "))
    name=input("Enter Name: ")
    course=input("Enter Course: ")
    marks=int(input("Enter Marks: "))
    
    student=Student(roll_no,name,course,marks)
    students=load_students()
    students.append(student.to_dict())
    save_data(students)
    print("Student data added successfully\n")

def display_students():
    students=load_students()
    if not students:
        print("\nNo student records found.\n")
        return
    for s in students:
        print(f"\nRoll No.: {s['roll_no']}\nName: {s['name']}\nCourse: {s['course']}\nMarks: {s['marks']}\n")
        print("-" *30)

def search_student():
    roll=int(input("\nEnter Roll No. to search: "))
    students=load_students()
    for s in students:
        if roll==s['roll_no']:
            print(f"\nStudent Record found.")
            print(f"\nName: {s['name']}\nCourse: {s['course']}\nMarks: {s['marks']}\n")
            return
    print("\nStudent record not found.")

def delete_student_data():
    roll=int(input("\nEnter Roll No. to delete student record: "))
    students=load_students()
    updated_list=[s for s in students if s['roll_no']!=roll]
    if len(students)==len(updated_list):
        print("\nStudent record not found.")
    else:
        save_data(updated_list) 
        print("Student record deleted successfully.\n")

def update_student_data():
    roll=int(input("\nEnter Roll No. to update: "))
    students=load_students()
    for s in students:
        if s['roll_no']==roll:
            print("Current details:")
            print(f"\nRoll No.: {s['roll_no']}\nName: {s['name']}\nCourse: {s['course']}\nMarks: {s['marks']}")
            s['name']=input("Enter new name: ")
            s['course']=input("Enter new course: ")
            s['marks']=float(input("Enter new marks: "))
            save_data(students)
            print("Student data updated successfully.\n")
            return
    print("\nStudent data not found.")

def menu():
    while True:
        print("\n-----Student Record Management-----")
        print("1.Add Student")
        print("2.Display Students data")
        print("3.Search Student")
        print("4.Delete Student record")
        print("5.Update Student record")
        print("6.Exit")

        choice=int(input("\nEnter your choice: "))

        if choice==1:
            add_student()
        elif choice==2:
            display_students()
        elif choice==3:     
            search_student()     
        elif choice==4:
            delete_student_data()
        elif choice==5:
            update_student_data()
        elif choice==6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__=='__main__':
    menu()
