ctc = float(input("Enter your Total CTC: "))
bonus = float(input("Enter your Bonus Amount: "))

income = ctc + bonus
print("Total Income:", income)

old_taxable = max(0, income - 220000)
old_tax = 0
if old_taxable <= 250000:
    old_tax = 0
elif old_taxable <= 500000:
    old_tax = (old_taxable - 250000) * 0.05
else:
    old_tax = 12500 + (old_taxable - 500000) * 0.2
new_tax = 0
if income <= 250000:
    new_tax = 0
elif income <= 500000:
    new_tax = (income - 250000) * 0.05
elif income <= 1000000:
    new_tax = 12500 + (income - 500000) * 0.2
else:
    new_tax = 12500 + 100000 + (income - 1000000) * 0.3

print("Old Regime Tax:", old_tax)
print("New Regime Tax:", new_tax)
