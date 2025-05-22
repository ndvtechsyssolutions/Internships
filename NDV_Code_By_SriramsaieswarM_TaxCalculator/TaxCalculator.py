ctc = float(input("Enter CTC: "))
bonus = float(input("Enter Bonus: "))
income = ctc + bonus
# --------------------Old Regime------------------------
old_taxable = income - 50000 - 200000  # Std deduction + HRA
old_tax = 0
if old_taxable > 1000000:
    old_tax = 112500 + (old_taxable - 1000000) * 0.3
elif old_taxable > 500000:
    old_tax = 12500 + (old_taxable - 500000) * 0.2
elif old_taxable > 250000:
    old_tax = (old_taxable - 250000) * 0.05
#------------------------- New Regime-----------------------------
new_tax = 0
t = income
slabs = [(300000, 0), (300000, 0.05), (300000, 0.1), (300000, 0.15), (300000, 0.2), (300000, 0.25), (1e9, 0.3)]
for s, r in slabs:
    if t > s:
        new_tax += s * r
        t -= s
    else:
        new_tax += t * r
        break
print("\nTotal Income:", income)
print("Old Regime Tax Deduction:", round(old_tax, 2))
print("New Regime Tax Deduction:", round(new_tax, 2))
if old_tax < new_tax:
    diff = new_tax - old_tax
    print(f"You save ₹{round(diff, 2)} by choosing the Old Regime.")
elif new_tax < old_tax:
    diff = old_tax - new_tax
    print(f"You save ₹{round(diff, 2)} by choosing the New Regime.")
else:
    print("Both regimes result in the same tax.")
