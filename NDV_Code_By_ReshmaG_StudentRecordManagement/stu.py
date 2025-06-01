lass Student:
    def __init__(self, id, name, branch, year):
        self.id = id
        self.name = name
        self.branch = branch
        self.year = year
students = []
while True:
    print("\n1. Add Student  2. Show Students  3. Exit")
    ch = input("Enter your choice: ")
    if ch == "1":
        sid = input("ID: ")
        name = input("Name: ")
        branch = input("Branch: ")
        year = input("Year: ")
        s = Student(sid, name, branch, year)
        students.append(s)
        print("Student added.")
    elif ch == "2":
        if len(students) == 0:
            print("No students yet.")
        else:
            for s in students:
                print("ID:", s.id, "| Name:", s.name, "| Branch:", s.branch, "| Year:", s.year)
    elif ch == "3":
        print("Thanks! Exiting.")
        break
    else:
        print("Invalid input.")
