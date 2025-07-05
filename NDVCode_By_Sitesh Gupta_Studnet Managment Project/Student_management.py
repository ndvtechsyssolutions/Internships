import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import os
import datetime

# --- Data Models ---

class Student:
    def __init__(self, Student_ID, name, age, gender, Course, contact, email,fee):
        self.Student_ID = Student_ID
        self.name = name
        self.age = age
        self.gender = gender
        self.Course = Course
        self.contact = contact
        self.email = email
        self.fee=fee

    def to_list(self):
        return [self.Student_ID, self.name, self.age, self.gender, self.Course, self.contact, self.email,self.fee]

class AttendanceRecord:
    def __init__(self, date, Student_ID, status):
        self.date = date
        self.Student_ID = Student_ID
        self.status = status  # Present/Absent/Late/Excused

    def to_list(self):
        return [self.date, self.Student_ID, self.status]

# --- Manager Classes ---

class StudentManager:
    def __init__(self):
        self.students = {}  # Student_ID: Student

    def add_student(self, student):
        if student.Student_ID in self.students:
            raise ValueError("Duplicate Student_ID")
        self.students[student.Student_ID] = student

    def update_student(self, Student_ID, **kwargs):
        if Student_ID not in self.students:
            raise ValueError("Student not found")
        for k, v in kwargs.items():
            setattr(self.students[Student_ID], k, v)

    def delete_student(self, Student_ID):
        if Student_ID in self.students:
            del self.students[Student_ID]

    def import_csv(self, filepath):
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] != "Student_ID":
                    if len(row) == 8: 
                        try:
                            student = Student(*row)
                            self.add_student(student)
                        except ValueError:
                            continue
                    else:
                        print(f"⚠️ Skipped row due to unexpected column count: {row}")
  

    def export_csv(self, filepath):
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Student_ID", "Name", "Age", "Gender", "Course", "Contact", "Email","Fee"])
                for s in self.students.values():
                    writer.writerow(s.to_list())

class AttendanceManager:
    def __init__(self):
        self.records = []  # List of AttendanceRecord

    def mark_attendance(self, date, Student_ID, status):
        self.records.append(AttendanceRecord(date, Student_ID, status))

    def get_attendance(self, date=None, Student_ID=None):
        return [r for r in self.records if (date is None or r.date == date) and (Student_ID is None or r.Student_ID == Student_ID)]

    def export_csv(self, filepath):
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Student_ID", "Status"])
            for r in self.records:
                writer.writerow(r.to_list())

# --- UI ---

class StudentManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NDVTechsys Student Management System")
        icon_path = os.path.join(os.path.dirname(__file__), "NDVTechsys_logo.ico")
        try:
            self.iconbitmap(icon_path)
        except Exception as e:
            print("⚠️ Icon loading failed:", e)


        self.geometry("1100x600")

        self.student_mgr = StudentManager()
        self.attendance_mgr = AttendanceManager()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        self.admission_tab = ttk.Frame(self.notebook)
        self.attendance_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.admission_tab, text="Student Admission")
        self.notebook.add(self.attendance_tab, text="Student Attendance")

        self.init_admission_tab()
        self.init_attendance_tab()
        self.import_students()

    # --- Admission Tab ---
    def init_admission_tab(self):
        frame = self.admission_tab

        # Filter Section (Top Right)
        filter_frame = ttk.Frame(frame)
        filter_frame.pack(anchor='ne', padx=10, pady=5)
        self.adm_filter_field_var = tk.StringVar(value="Student_ID")
        ttk.Label(filter_frame, text="Search by:").grid(row=0, column=0)
        ttk.Combobox(filter_frame, textvariable=self.adm_filter_field_var, values=["Student_ID", "Name"], width=15).grid(row=0, column=1)
        self.adm_filter_value_var = tk.StringVar()
        ttk.Entry(filter_frame, textvariable=self.adm_filter_value_var, width=15).grid(row=0, column=2, padx=5)
        ttk.Button(filter_frame, text="Search", command=self.filter_students).grid(row=0, column=3, padx=2)
        ttk.Button(filter_frame, text="Show All", command=self.refresh_student_table).grid(row=0, column=4, padx=2)

        # Form
        form_frame = ttk.LabelFrame(frame, text="Add/Update Student")
        form_frame.pack(side='top', fill='x', padx=10, pady=5)

        labels = ["Student_ID", "Name", "Age", "Gender", "Course", "Contact", "Email","Fee"]
        self.adm_vars = {l: tk.StringVar() for l in labels}
        for i, l in enumerate(labels):
            ttk.Label(form_frame, text=l).grid(row=0, column=i)
            ttk.Entry(form_frame, textvariable=self.adm_vars[l], width=12).grid(row=1, column=i)

        ttk.Button(form_frame, text="Add Admission", command=self.add_admission).grid(row=1, column=len(labels), padx=5)
        ttk.Button(form_frame, text="Import CSV", command=self.import_students).grid(row=1, column=len(labels)+1, padx=5)
        ttk.Button(form_frame, text="Export CSV", command=self.export_students).grid(row=1, column=len(labels)+2, padx=5)

        # Table
        columns = labels
        self.adm_tree = ttk.Treeview(frame, columns=columns, show='headings', height=20)
        for col in columns:
            self.adm_tree.heading(col, text=col)
            self.adm_tree.column(col, width=100)
        self.adm_tree.pack(fill='both', expand=True, padx=10, pady=5)
        self.adm_tree.bind('<Double-1>', self.edit_student)

        # Delete/Update
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x', padx=10, pady=2)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_student).pack(side='left')
        ttk.Button(btn_frame, text="Update Selected", command=self.update_student).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Exit", command=self.safe_exit).pack(side='right', padx=5)
        self.refresh_student_table()

    def safe_exit(self):
        self.student_mgr.export_csv("students_backup.csv")
        self.attendance_mgr.export_csv("attendance_backup.csv")
        self.destroy()


    def import_students(self):
        default_path = "students_backup.csv"
        if os.path.exists(default_path):
            self.student_mgr.import_csv(default_path)
            self.refresh_student_table()

    def add_admission(self):
        try:
            student = Student(
                self.adm_vars["Student_ID"].get(),
                self.adm_vars["Name"].get(),
                self.adm_vars["Age"].get(),
                self.adm_vars["Gender"].get(),
                self.adm_vars["Course"].get(),
                self.adm_vars["Contact"].get(),
                self.adm_vars["Email"].get(),
                self.adm_vars["Fee"].get()
            )
            self.student_mgr.add_student(student)
            self.refresh_student_table()
            for v in self.adm_vars.values():
                v.set("")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        selected = self.adm_tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a student to update.")
            return

        old_Student_ID = self.adm_tree.item(selected[0])['values'][0]

        try:
            new_student = Student(
            self.adm_vars["Student_ID"].get(),
            self.adm_vars["Name"].get(),
            self.adm_vars["Age"].get(),
            self.adm_vars["Gender"].get(),
            self.adm_vars["Course"].get(),
            self.adm_vars["Contact"].get(),
            self.adm_vars["Email"].get(),
            self.adm_vars["Fee"].get()
            )

            self.student_mgr.update_student(
                Student_ID=new_student.Student_ID,
                name=new_student.name,
                age=new_student.age,
                gender=new_student.gender,
                Course=new_student.Course,
                contact=new_student.contact,
                email=new_student.email,
                fee=new_student.fee
            )   

            self.refresh_student_table()
            for v in self.adm_vars.values():
                v.set("")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


    def filter_students(self):
        field = self.adm_filter_field_var.get()
        value = self.adm_filter_value_var.get().lower()
        self.adm_tree.delete(*self.adm_tree.get_children())

        for s in self.student_mgr.students.values():
            attr = getattr(s, field.lower().replace(" ", "_"), "")
            if value in str(attr).lower():
                self.adm_tree.insert('', 'end', values=s.to_list())  


    def refresh_student_table(self):
        for row in self.adm_tree.get_children():
            self.adm_tree.delete(row)
        for s in self.student_mgr.students.values():
            data = s.to_list()
            data[-1] = f"₹{data[-1]}"  # Format the fee with rupee symbol
            self.adm_tree.insert('', 'end', values=data)

    def delete_student(self):
        selected = self.adm_tree.selection()
        for item in selected:
            Student_ID = self.adm_tree.item(item)['values'][0]
            self.student_mgr.delete_student(Student_ID)
        self.refresh_student_table()

    def edit_student(self, event):
        item = self.adm_tree.selection()[0]
        values = self.adm_tree.item(item)['values']
        for i, l in enumerate(self.adm_vars):
            self.adm_vars[l].set(values[i])

    def import_students(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.student_mgr.import_csv(path)
            self.refresh_student_table()

    def export_students(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if path:
            self.student_mgr.export_csv(path)

    # --- Attendance Tab ---
    def init_attendance_tab(self):
        frame = self.attendance_tab

        # Date picker
        date_frame = ttk.Frame(frame)
        date_frame.pack(fill='x', padx=10, pady=5)
        # Filter Controls (Top Right)
        filter_frame = ttk.Frame(frame)
        filter_frame.pack(anchor='ne', padx=10, pady=5)

        self.att_filter_field_var = tk.StringVar(value="Student_ID")
        ttk.Label(filter_frame, text="Search by:").grid(row=0, column=0)
        ttk.Combobox(filter_frame, textvariable=self.att_filter_field_var, values=["Student_ID", "Name"], width=10).grid(row=0, column=1)

        self.att_filter_value_var = tk.StringVar()
        ttk.Entry(filter_frame, textvariable=self.att_filter_value_var, width=15).grid(row=0, column=2, padx=5)

        ttk.Button(filter_frame, text="Search", command=self.filter_attendance).grid(row=0, column=3, padx=2)
        ttk.Button(filter_frame, text="Show All", command=self.load_attendance_students).grid(row=0, column=4, padx=2)  
        ttk.Label(date_frame, text="Date (YYYY-MM-DD):").pack(side='left')
        self.att_date_var = tk.StringVar(value=datetime.date.today().isoformat())
        ttk.Entry(date_frame, textvariable=self.att_date_var, width=12).pack(side='left')

        ttk.Button(date_frame, text="Load Students", command=self.load_attendance_students).pack(side='left', padx=5)
        ttk.Button(date_frame, text="Export Attendance", command=self.export_attendance).pack(side='left', padx=5)

        # Table
        columns = ["Student_ID", "Name", "Status"]
        self.att_tree = ttk.Treeview(frame, columns=columns, show='headings', height=20)
        for col in columns:
            self.att_tree.heading(col, text=col)
            self.att_tree.column(col, width=120)
        self.att_tree.pack(fill='both', expand=True, padx=10, pady=5)

        # Mark buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x', padx=10, pady=2)
        ttk.Button(btn_frame, text="Mark Selected Present", command=lambda: self.mark_selected_attendance("Present")).pack(side='left')
        ttk.Button(btn_frame, text="Mark All Present", command=lambda: self.mark_all_attendance("Present")).pack(side='left')
        ttk.Button(btn_frame, text="Mark Selected Absent", command=lambda: self.mark_selected_attendance("Absent")).pack(side='left')

    def load_attendance_students(self):
        self.att_tree.delete(*self.att_tree.get_children())
        date = self.att_date_var.get()
        for s in self.student_mgr.students.values():
            self.att_tree.insert('', 'end', values=(s.Student_ID, s.name, ""))
    
    def filter_attendance(self):
        field = self.att_filter_field_var.get()
        value = self.att_filter_value_var.get().lower()
        date = self.att_date_var.get()
    
        self.att_tree.delete(*self.att_tree.get_children())

        for s in self.student_mgr.students.values():
            attr = getattr(s, field.lower().replace(" ", "_"), "")
            if value in str(attr).lower():
                status = ""
                for r in self.attendance_mgr.get_attendance(date, s.Student_ID):
                    status = r.status
            self.att_tree.insert('', 'end', values=(s.Student_ID, s.name, status))

    def mark_selected_attendance(self, status):
        date = self.att_date_var.get()
        for item in self.att_tree.selection():
            Student_ID = self.att_tree.item(item)['values'][0]
            self.att_tree.set(item, "Status", status)
            self.attendance_mgr.mark_attendance(date, Student_ID, status)

    def mark_all_attendance(self, status):
        date = self.att_date_var.get()
        for item in self.att_tree.get_children():
            Student_ID = self.att_tree.item(item)['values'][0]
            self.att_tree.set(item, "Status", status)
            self.attendance_mgr.mark_attendance(date, Student_ID, status)

    def export_attendance(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if path:
            self.attendance_mgr.export_csv(path)

if __name__ == "__main__":
    app = StudentManagementApp()
    app.mainloop()
