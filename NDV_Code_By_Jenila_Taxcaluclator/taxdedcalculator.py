ctc = float(input("Enter your Total CTC (₹): "))
bonus = float(input("Enter your Total Bonus (₹): "))
total_income = ctc + bonus
print("\nTotal Income (CTC + Bonus): ₹", total_income)
standard_deduction = 50000
hra = 100000
deduction_80c = 150000
taxable_old = total_income - standard_deduction - hra - deduction_80c
if taxable_old <= 250000:
    tax_old = 0
elif taxable_old <= 500000:
    tax_old = (taxable_old - 250000) * 0.05
elif taxable_old <= 1000000:
    tax_old = 12500 + (taxable_old - 500000) * 0.20
else:
    tax_old = 112500 + (taxable_old - 1000000) * 0.30
if total_income <= 300000:
    tax_new = 0
elif total_income <= 600000:
    tax_new = (total_income - 300000) * 0.05
elif total_income <= 900000:
    tax_new = 15000 + (total_income - 600000) * 0.10
elif total_income <= 1200000:
    tax_new = 45000 + (total_income - 900000) * 0.15
elif total_income <= 1500000:
    tax_new = 90000 + (total_income - 1200000) * 0.20
else:
    tax_new = 150000 + (total_income - 1500000) * 0.30
print("Tax under Old Regime: ₹", tax_old)
print("Tax under New Regime: ₹", tax_new)
