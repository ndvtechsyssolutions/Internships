import json
import os

# Create a json file where the data will be saved
data_file='student.json'

class student:
    def __init__(self,student_id,name,branch,year):
         self.student_id=student_id
         self.name=name
         self.branch=branch
         self.year=year
        
    def to_dict(self):
         return{
              'Student ID':self.student_id,
              'Name':self.name,
              'Branch':self.branch,
              'Year':self.year,
         }

class Manager:
    def __init__(self):
          self.students=[]
          self.load_data()

    def load_data(self):
         if os.path.exists(data_file):
              with open(data_file,'r') as f:
                   data=json.load(f)
                   for item in data:
                        stud=student(item['Student ID'],
                                     item['Name'],
                                     item['Branch'],
                                     item['Year']
                                     )
                        self.students.append(stud)

    def save_data(self):
         with open(data_file,'w') as f:
              json.dump([s.to_dict() for s in self.students],f,indent=4)

     # Insert Student record
    def add_student(self):
         student_id=input("Enter student id:")
         name=input("enter student name:")
         branch=input("enter student branch:")
         year=input("enter the year:")

         stud=student(student_id,name,branch,year)
         self.students.append(stud)
         self.save_data()
         print("Student record Added Successfully!!\n")

     # To view the student records
    def view_student(self):
         if not self.students:
              print("No records found\n")
              return
         print("-"*60)
         print(f"{'ID':<10}{'Name':<20}{'Branch':<15}{'Year':<5}")
         print("-"*60)
         for student in self.students:
              print(f"{student.student_id:<10} {student.name:<20} {student.branch:<15} {student.year:<5}")
              print("-"*60)
         
         # Update Student record by using student id
    def update_student(self):
         student_id=input("Enter student ID to update:")
         for student in self.students:
              if student.student_id==student_id:
                   student.name=input(f"Enter new name(current:{student.name}):") or student.name
                   student.branch=input(f"Enter new branch(current:{student.branch}):") or student.branch
                   student.year=input(f"Enter new year(current:{student.year}):") or student.year
                   self.save_data()
                   print("Student record updated Successfully!\n")
                   return
              print("Students not found.\n")

     # Delete student record
    def delete_student(self):
         student_id=input("Enter Student ID to delete:")
         for student in self.students:
              if student.student_id==student_id:
                   self.students.remove(student)
                   self.save_data()
                   print("Student record deleted successfully!\n")
                   return 
              print("Student not Found.\n ")

def main():
     manager=Manager()
     while True:
          print("\n------Student Record Management------")
          print("1.ADD Student")
          print("2.VIEW ALL Student")
          print("3.UPDATE Student")
          print("4.DELETE Student")
          print("5.EXIT")

          choice=input("Enter your choice:")

          if choice=='1':
               manager.add_student()
          elif choice=='2':
               manager.view_student()
          elif choice=='3':
               manager.update_student()
          elif choice=='4':
               manager.delete_student()
          elif choice=='5':
               print("Exiting program!!")
               break
          else:
               print("Invalid Choice. Please enter again:\n")

if __name__=="__main__":
     main()
