# student.py

class Student:
    def __init__(self, student_id, name, branch, year, marks):
        self.student_id = student_id
        self.name = name
        self.branch = branch
        self.year = year
        self.marks = marks

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "branch": self.branch,
            "year": self.year,
            "marks": self.marks
        }

    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, Branch: {self.branch}, "
                f"Year: {self.year}, Marks: {self.marks}")
