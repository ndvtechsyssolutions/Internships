def calculate_old_regime_tax(income):
    deductions = 50000 + 150000 + 200000  # Standard deduction + 80C + HRA (example)
    taxable_income = max(0, income - deductions)
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = 0.05 * (taxable_income - 250000)
    elif taxable_income <= 1000000:
        tax = 12500 + 0.2 * (taxable_income - 500000)
    else:
        tax = 112500 + 0.3 * (taxable_income - 1000000)
    return tax
def calculate_new_regime_tax(income):
    slabs = [(0, 300000, 0), (300001, 600000, 0.05), (600001, 900000, 0.1),
             (900001, 1200000, 0.15), (1200001, 1500000, 0.2), (1500001, float('inf'), 0.3)]
    tax = 0
    for lower, upper, rate in slabs:
        if income > lower:
            taxable = min(income, upper) - lower
            tax += taxable * rate
    return tax
# User Input
ctc = float(input("Enter total CTC: "))
bonus = float(input("Enter total bonus amount: "))
total_income = ctc + bonus
# Calculations
old_tax = calculate_old_regime_tax(total_income)
new_tax = calculate_new_regime_tax(total_income)
# Comparison
print(f"\nTotal Income (with bonus): ₹{total_income:.2f}")
print(f"Old Regime Tax: ₹{old_tax:.2f}")
print(f"New Regime Tax: ₹{new_tax:.2f}")
if old_tax < new_tax:
    print("Old Regime is more beneficial.")
elif new_tax < old_tax:
    print("New Regime is more beneficial.")
else:
    print("Both regimes result in the same tax.")