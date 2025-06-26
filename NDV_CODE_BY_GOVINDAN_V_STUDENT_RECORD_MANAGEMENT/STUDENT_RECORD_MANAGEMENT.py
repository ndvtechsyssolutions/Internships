# Student records management system  (console app)

# JSON : store data as records 
# Class ,objects , functions / methods 
# file system 

import json 
import os 

class Student:
    # constructor 
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks 

    def to_dict(self):
        return {"name":self.name,"roll_no":self.roll_no,"marks":self.marks}
    def display(self):
        print("name is..",self.name)
        print("roll_no is..",self.roll_no)
        print("marks are ..",self.marks)
    
class StudentManager:
    FILE_NAME="students.json"

    def load_data(self):
        if not os.path.exists(self.FILE_NAME):
            return[] 
        with open(self.FILE_NAME,'r') as file:
            return json.load(file)
        
                
