import json
import os

class Students:
    
    def __init__(self,id,name,branch,year,marks):
        self.id = id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks
    
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "branch":self.branch,
            "year":self.year,
            "marks":self.marks
        }
    
    def display(self):
        print("ID: ",self.id)
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Year: ",self.year)
        print("Marks: ",self.marks)

class Student_management:
    file_name = "student_data.json"
    def __init__(self,file_name):
        self.file_name= file_name
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_name):
            return []
        try:
            with open(self.file_name,'r') as file:
                return json.load(file)
        except Exception as e:
            print("Error Occured as: ",e)
    
    def save_data(self):
        try:
            with open(self.file_name,'w') as file:
                json.dump(self.data,file,indent=4)
        except Exception as e:
            print("Error Occured as: ",e)
    
    def add(self):
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = int(input("Enter Year: "))
        marks = float(input("Enter Marks: "))

        student = Students(id,name,branch,year,marks)
        self.data.append(student.to_dict())
        self.save_data()
        print("Student added Successfully\n")
    
    def display_students(self):
        if not self.data:
            print("No Students Found.")
            return
        for std_dict in self.data:
            student = Students(**std_dict)
            student.display()
            print("-" * 20)
    
    def update(self):
        ids = int(input("Enter ID: "))
        for student in self.data:
            if ids==student["id"]:
                student["name"] = input("Update Name to: ")
                student["branch"] = input("Update Branch to: ")
                student["year"] = int(input("Update Year to: "))
                student["marks"] = float(input("Update Marks to: "))
                self.save_data()
                print("Studetn details Updated!\n")
    
    def disp_stud_details(self):
        ids = int(input("Enter ID: "))
        for student in self.data:
            if ids==student["id"]:
                a = Students(**student)
                a.display()
    
    def delete(self):
        ids = int(input("Enter ID: "))
        self.data = [s for s in self.data if s["id"]!=ids]
        self.save_data()
        print("Student Deleted Successfully.\n")

if __name__ == "__main__":
    manager = Student_management("student_data.json")

    while True:
        print("To Add Student press - 1")
        print("To Delete Student press - 2")
        print("To Update Student press - 3")
        print("To Display All Student Details press - 4")
        print("To Display A Student Details press - 5")
        print("TO EXIT PRESS - 0")
        
        choice = int(input("Enter your choice: "))
        if choice==0:
            break
        elif choice==1:
            manager.add()
            print("-"*20)
        elif choice==2:
            manager.delete()
            print("-"*20)
        elif choice==3:
            manager.update()
            print("-"*20)
        elif choice==4:
            manager.display_students()
            print("-"*20)
        elif choice==5:
            manager.disp_stud_details()
            print("-"*20)
        else:
            print("Enter Correct Choice")