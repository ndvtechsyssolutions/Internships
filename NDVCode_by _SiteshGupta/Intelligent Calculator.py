import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
import math
import os

# ---------- Utility Functions ----------
def format_currency(val):
    return f"₹{val:,.2f}"

def save_session(data, scenario):
    df = pd.DataFrame([data])
    filename = f"{scenario}_history.csv"
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)

def load_history(scenario):
    filename = f"{scenario}_history.csv"
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame()

# ---------- Scenario Frames ----------
class HomeLoanFrame(ttk.Frame):
    def __init__(self, parent, recommend_callback):
        super().__init__(parent)
        self.recommend_callback = recommend_callback
        self.create_widgets()

    def create_widgets(self):
        # Inputs
        ttk.Label(self, text="Loan Amount:").grid(row=0, column=0, sticky="e")
        self.loan_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.loan_var).grid(row=0, column=1)

        ttk.Label(self, text="Tenure (years):").grid(row=1, column=0, sticky="e")
        self.tenure_var = tk.IntVar()
        ttk.Entry(self, textvariable=self.tenure_var).grid(row=1, column=1)

        ttk.Label(self, text="Interest Rate (% p.a.):").grid(row=2, column=0, sticky="e")
        self.rate_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.rate_var).grid(row=2, column=1)

        ttk.Label(self, text="Monthly Income:").grid(row=3, column=0, sticky="e")
        self.income_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.income_var).grid(row=3, column=1)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=10)

        self.result = tk.Text(self, width=60, height=12, state='disabled')
        self.result.config(bg="white", font=("Segoe UI", 10), relief="solid", bd=2)
        self.result.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)




    def calculate(self):
        try:
            P = Decimal(str(self.loan_var.get()))
            N = int(self.tenure_var.get()) * 12
            R = Decimal(str(self.rate_var.get())) / Decimal('1200')
            income = Decimal(str(self.income_var.get()))

            emi = (P * R * (1 + R) ** N) / ((1 + R) ** N - 1)
            emi = emi.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            total_payment = emi * N
            total_interest = total_payment - P

            # Recommendation
            alert = ""
            if emi > income * Decimal('0.4'):
                alert = "⚠️ EMI exceeds 40% of your income. Consider reducing loan or increasing tenure.\n"
            else:
                alert = "👍 EMI is within a safe range.\n"

            # Save session
            session_data = {
                "Loan Amount": float(P),
                "Tenure (years)": N // 12,
                "Interest Rate": float(R * 1200),
                "Monthly Income": float(income),
                "EMI": float(emi),
                "Total Interest": float(total_interest)
            }
            save_session(session_data, "home_loan")

            # Output
            self.result.config(state='normal')
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, f"{alert}\n")
            self.result.insert(tk.END, f"Monthly EMI: {format_currency(float(emi))}\n")
            self.result.insert(tk.END, f"Total Interest: {format_currency(float(total_interest))}\n")
            self.result.insert(tk.END, f"Total Payment: {format_currency(float(total_payment))}\n")
            self.result.config(state='disabled')

            self.recommend_callback(alert)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

class FreelancerFrame(ttk.Frame):
    def __init__(self, parent, recommend_callback):
        super().__init__(parent)
        self.recommend_callback = recommend_callback
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Monthly Projects:").grid(row=0, column=0, sticky="e")
        self.projects_var = tk.IntVar()
        ttk.Entry(self, textvariable=self.projects_var).grid(row=0, column=1)

        ttk.Label(self, text="Expected Rate per Project:").grid(row=1, column=0, sticky="e")
        self.rate_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.rate_var).grid(row=1, column=1)

        ttk.Label(self, text="Monthly Expenses:").grid(row=2, column=0, sticky="e")
        self.expenses_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.expenses_var).grid(row=2, column=1)

        ttk.Button(self, text="Forecast", command=self.calculate).grid(row=3, column=0, columnspan=2, pady=10)
        self.result = tk.Text(self, width=60, height=12, state='disabled')
        self.result.config(bg="white", font=("Segoe UI", 10), relief="solid", bd=2)
        self.result.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def calculate(self):
        try:
            projects = int(self.projects_var.get())
            rate = Decimal(str(self.rate_var.get()))
            expenses = Decimal(str(self.expenses_var.get()))

            monthly_income = projects * rate
            net_income = monthly_income - expenses
            three_months = net_income * 3

            # Recommendation
            if net_income < Decimal('0'):
                alert = "⚠️ Your expenses exceed your income. Consider increasing rates or reducing costs.\n"
            else:
                alert = "👍 Your freelance plan is profitable.\n"

            session_data = {
                "Projects": projects,
                "Rate": float(rate),
                "Expenses": float(expenses),
                "Net Income": float(net_income)
            }
            save_session(session_data, "freelancer")

            self.result.config(state='normal')
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, f"{alert}\n")
            self.result.insert(tk.END, f"Monthly Net Income: {format_currency(float(net_income))}\n")
            self.result.insert(tk.END, f"3-Month Forecast: {format_currency(float(three_months))}\n")
            self.result.config(state='disabled')

            self.recommend_callback(alert)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

class EducationFrame(ttk.Frame):
    def __init__(self, parent, recommend_callback):
        super().__init__(parent)
        self.recommend_callback = recommend_callback
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Tuition per Year:").grid(row=0, column=0, sticky="e")
        self.tuition_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.tuition_var).grid(row=0, column=1)

        ttk.Label(self, text="Books per Year:").grid(row=1, column=0, sticky="e")
        self.books_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.books_var).grid(row=1, column=1)

        ttk.Label(self, text="Hostel per Year:").grid(row=2, column=0, sticky="e")
        self.hostel_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.hostel_var).grid(row=2, column=1)

        ttk.Label(self, text="Inflation Rate (%):").grid(row=3, column=0, sticky="e")
        self.inflation_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.inflation_var).grid(row=3, column=1)

        ttk.Button(self, text="Calculate", command=self.calculate).grid(row=4, column=0, columnspan=2, pady=10)

        self.result = tk.Text(self, width=60, height=12, state='disabled')
        self.result.config(bg="white", font=("Segoe UI", 10), relief="solid", bd=2)
        self.result.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def calculate(self):
        try:
            tuition = Decimal(str(self.tuition_var.get()))
            books = Decimal(str(self.books_var.get()))
            hostel = Decimal(str(self.hostel_var.get()))
            inflation = Decimal(str(self.inflation_var.get())) / Decimal('100')

            total = Decimal('0')
            breakdown = ""
            for year in range(1, 5):
                year_cost = (tuition + books + hostel) * ((Decimal('1') + inflation) ** (year - 1))
                total += year_cost
                breakdown += f"Year {year}: {format_currency(float(year_cost))}\n"

            per_semester = total / 8

            alert = "👍 Plan for inflation to avoid surprises.\n"
            session_data = {
                "Tuition": float(tuition),
                "Books": float(books),
                "Hostel": float(hostel),
                "Inflation": float(inflation * 100),
                "Total Cost": float(total)
            }
            save_session(session_data, "education")

            self.result.config(state='normal')
            self.result.delete(1.0, tk.END)
            self.result.insert(tk.END, f"{alert}\n")
            self.result.insert(tk.END, f"4-Year Total: {format_currency(float(total))}\n")
            self.result.insert(tk.END, f"Per Semester: {format_currency(float(per_semester))}\n")
            self.result.insert(tk.END, f"\nBreakdown:\n{breakdown}")
            self.result.config(state='disabled')

            self.recommend_callback(alert)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

# ---------- History/Compare Panel ----------
class HistoryFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Select Scenario:").grid(row=0, column=0, sticky="e")
        self.scenario_var = tk.StringVar()
        self.dropdown = ttk.Combobox(self, textvariable=self.scenario_var, state="readonly")
        self.dropdown['values'] = ("home_loan", "freelancer", "education")
        self.dropdown.grid(row=0, column=1)
        self.dropdown.bind("<<ComboboxSelected>>", self.load_history)

        self.tree = ttk.Treeview(self, columns=(), show="headings")
        self.tree.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def load_history(self, event=None):
        scenario = self.scenario_var.get()
        df = load_history(scenario)
        for col in self.tree["columns"]:
            self.tree.heading(col, text="")
        self.tree.delete(*self.tree.get_children())
        if not df.empty:
            self.tree["columns"] = list(df.columns)
            for col in df.columns:
                self.tree.heading(col, text=col)
            for _, row in df.iterrows():
                self.tree.insert("", "end", values=list(row))
        else:
            self.tree["columns"] = ()
            self.tree.insert("", "end", values=("No history found.",))

# ---------- Main Application ----------
class LifeFlowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LifeFlow - Intelligent Scenario Calculator")
        self.iconbitmap("NDVTechsys_logo.ico")
        self.geometry("700x600")
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TNotebook.Tab', font=('Segoe UI', 11, 'bold'))
        self.style.configure('TButton', font=('Segoe UI', 10))
        self.create_widgets()

    def create_widgets(self):
        # Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=50, pady=10)

        # Tabs
        self.home_loan_tab = HomeLoanFrame(self.notebook, self.show_recommendation)
        self.freelancer_tab = FreelancerFrame(self.notebook, self.show_recommendation)
        self.education_tab = EducationFrame(self.notebook, self.show_recommendation)
        self.history_tab = HistoryFrame(self.notebook)

        self.notebook.add(self.home_loan_tab, text="🏠 Home Loan")
        self.notebook.add(self.freelancer_tab, text="🧾 Freelancer")
        self.notebook.add(self.education_tab, text="🎓 Education")
        self.notebook.add(self.history_tab, text="📊 Compare Sessions")

        # Recommendation Panel
        self.recommend_label = ttk.Label(self, text="", foreground="#e67e22", font=('Segoe UI', 10, 'italic'))
        self.recommend_label.pack(side="bottom", pady=5)

    def show_recommendation(self, text):
        self.recommend_label.config(text=text)

if __name__ == "__main__":
    app = LifeFlowApp()
    app.mainloop()
