ctc = float(input("Enter your CTC: ₹"))
bonus = float(input("Enter your bonus: ₹"))
total_income = ctc + bonus
standard_deduction = 50000
section_80c = 150000
taxable_old = max(0, total_income - standard_deduction - section_80c)
taxable_new = total_income
tax_old = (max(0, taxable_old - 1000000)*0.3 + max(0, min(taxable_old,1000000)-500000)*0.2 + max(0, min(taxable_old,500000)-250000)*0.05)
tax_new = (max(0, taxable_new - 1500000)*0.3 + max(0, min(taxable_new,1500000)-1200000)*0.2 + max(0, min(taxable_new,1200000)-900000)*0.15 + max(0, min(taxable_new,900000)-600000)*0.1 + max(0, min(taxable_new,600000)-300000)*0.05)
print(f"\nTotal Income: ₹{total_income:,.0f}")
print(f"Old Regime Tax: ₹{tax_old:,.0f}")
print(f"New Regime Tax: ₹{tax_new:,.0f}")
if tax_old < tax_new:
    print(f"You Save ₹{tax_new - tax_old:,.0f} more using Old Regime")
else:
    print(f"You Save ₹{tax_old - tax_new:,.0f} more using New Regime")
