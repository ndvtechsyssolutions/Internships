# Basic Python Tax Calculator for Old vs New Regime

print("==== TAX DEDUCTION CALCULATOR ====")

# Input
ctc = float(input("Enter your CTC (₹): "))
bonus = float(input("Enter your Bonus (₹): "))

# Total income
total_income = ctc + bonus
print("Total Income (CTC + Bonus): ₹", total_income)

# ---- Old Regime ----
# Standard deduction
standard_deduction = 50000
hra = 20000
sec_80c = 150000  # Maximum under Section 80C

# Total deductions under old regime
total_deductions_old = standard_deduction + hra + sec_80c
taxable_income_old = total_income - total_deductions_old

# Calculate old regime tax
if taxable_income_old <= 250000:
    old_tax = 0
elif taxable_income_old <= 500000:
    old_tax = (taxable_income_old - 250000) * 0.05
elif taxable_income_old <= 1000000:
    old_tax = (250000 * 0.05) + (taxable_income_old - 500000) * 0.20
else:
    old_tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income_old - 1000000) * 0.30

old_tax += old_tax * 0.04  # 4% cess

# ---- New Regime ----
taxable_income_new = total_income

# Calculate new regime tax
if taxable_income_new <= 300000:
    new_tax = 0
elif taxable_income_new <= 600000:
    new_tax = (taxable_income_new - 300000) * 0.05
elif taxable_income_new <= 900000:
    new_tax = (300000 * 0.05) + (taxable_income_new - 600000) * 0.10
elif taxable_income_new <= 1200000:
    new_tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income_new - 900000) * 0.15
elif taxable_income_new <= 1500000:
    new_tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income_new - 1200000) * 0.20
else:
    new_tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income_new - 1500000) * 0.30

new_tax += new_tax * 0.04  # 4% cess

# Output
print("Old Regime Tax Deduction: ₹", round(old_tax))
print("New Regime Tax Deduction: ₹", round(new_tax))

# Comparison
if old_tax < new_tax:
    print("You save ₹", round(new_tax - old_tax), "more using the Old Regime.")
elif new_tax < old_tax:
    print("You save ₹", round(old_tax - new_tax), "more using the New Regime.")
else:
    print("Both regimes give the same tax. Choose either.")