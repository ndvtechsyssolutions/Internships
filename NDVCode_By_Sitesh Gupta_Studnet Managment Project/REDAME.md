# NDVTechsys Student Management System

A GUI-based Python application to manage student records and track daily attendance — complete with CSV import/export, student filters, fee tracking in INR, and session persistence.

Built using **Tkinter**, this tool empowers schools, trainers, or administrators to effortlessly manage and monitor student data with a clean and interactive interface.

---

## 📦 Features

### 📝 Student Admission
- Add students with fields: `Student_ID`, `Name`, `Age`, `Gender`, `Cours`, `Contact`, `Email`, and `Fee (₹)`
- Import/export student data to/from CSV
- Filter students by **Student_ID** or **Name**
- Double-click to edit and update any student's details
- Exit button with auto-save functionality

### 📅 Attendance Tab
- View students by selected date
- Mark selected or all students as **Present** or **Absent**
- Filter students by `Student_ID` or `Name` for attendance marking
- Attendance export in CSV format
- Exit button with auto-save for all attendance records

### 💾 Auto Data Persistence
- Students and attendance data are **auto-saved** on exit to CSV (`students_backup.csv`, `attendance_backup.csv`)
- Automatically loaded on the next run — no data loss!

### 💸 INR Fee Display
- Fees are automatically shown with the **₹** symbol in the UI

---

## 🚀 How to Run

### ✅ Prerequisites

- Python 3.9 or above installed ([Download here](https://www.python.org/downloads/))
- Basic knowledge of running Python scripts
- No external libraries required — only built-in modules used!

### 🖥 Setup Steps

1. **Clone or Download** this project:
```
git clone https://github.com/your-username/ndvtechsys-student-management.git
```
Or simply download the `.zip` folder and extract it.

2. **Run the project**:
Navigate to the project directory and run:

------------------------------
## 📁 File Structure
```
NDVTechsys_Student_Management/
│
├── Student_Management.py        # 🧠 Main GUI application with all tabs and logic
├── students_backup.csv          # 💾 Auto-saved student data (created on app exit)
├── attendance_backup.csv        # 💾 Auto-saved attendance data (created on app exit)
├── NDVTechsys_logo.ico          # 🎨 Optional icon file for your window
├── README.md                    # 📘 Documentation with setup & feature guide
└── __pycache__/                 # ⚙️ (Auto-created by Python for performance)
```


---

## 🛠 Developer Notes

- Built using `tkinter`, `ttk`, `csv`, `datetime`, and `os`
- You can rename fields (`Student_ID`, `Cours`) as needed in the labels and `Student` class
- Data validation for numeric `Fee` or contact format can be added easily
- For extended versions:
  - Add SQLite for more robust storage
  - Integrate charts for attendance analytics
  - Generate student ID cards in PDF

---

## 🧠 Author & Maintainer

**Created by:** Sitesh  
**Project scope:** Real-world school/student data manager with clean GUI  
Want to collaborate or expand this? Reach out!

---

## 📜 License

This project is licensed for educational and development use. Share, modify, but please credit the original creator if you fork or build upon it.









