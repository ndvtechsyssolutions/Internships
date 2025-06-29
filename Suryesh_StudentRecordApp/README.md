# 🧾 Student Record Management System (Console App) – Internship Project

This is a **console-based student management application** built in Python as part of an internship project. It allows users to manage student records with full CRUD operations, search, statistics, and file persistence.

---

## 📌 Features

- ✅ Add, View, Update, Delete student records
- 🔍 Search student by **ID** or **Name**
- 📊 View statistics: **Top Scorer**, **Average Marks**
- 💾 Save and Load student data from a **JSON file** (`students.json`)
- ✅ Input validation for all fields (ID, Name, Branch, Year, Marks)

---

## 🧠 Technologies Used

- **Python 3**
- Standard Libraries: `json`, `re`
- No external dependencies required

---

## 🗂️ Project Structure
```
StudentManagementSystem/
│
├── student.py # Defines the Student class
├── student_manager.py # Core logic for managing student records
├── main.py # Entry point and menu-driven interface
├── students.json # JSON file to save/load data
└── README.md # Project documentation
```

---


## ▶️ How to Run

### Step 1: Open terminal and navigate to the project folder

```bash
cd F:\StudentManagementSystem
```
```
python main.py
```
---
## 💾 File Persistence (Manual)

- Use **menu option 9** → **Save to File** to save all student data to `students.json`
- Use **menu option 10** → **Load from File** to reload saved data from `students.json`

This implementation fulfills the **bonus requirement** for file I/O as mentioned in the assignment.

## 📚 Sample Run

====== **STUDENT MANAGEMENT SYSTEM** ======

1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search by ID
6. Search by Name
7. Top Scorer
8. Average Marks
9. Save to File
10. Load from File
11. Exit

- Enter your choice (1-11): 1
- Enter Student ID: 1001
- Enter Name: Suryesh
- Enter Branch: CSE1
- Enter Year: 2023
- Enter Marks: 89.5
- ✅ Student added successfully!

## ✍️ Author
- **Suryesh Pandey**
- B.Sc (Computing), Bennett University
- 🧪 Internship Project — **Vertunexa**