def old_regime_tax(income):
    income -= 50000 + 150000  # standard + 80C
    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return 12500 + (income - 500000) * 0.2
    else:
        return 112500 + (income - 1000000) * 0.3

def new_regime_tax(income):
    if income <= 300000:
        return 0
    elif income <= 600000:
        return (income - 300000) * 0.05
    elif income <= 900000:
        return 15000 + (income - 600000) * 0.1
    elif income <= 1200000:
        return 45000 + (income - 900000) * 0.15
    elif income <= 1500000:
        return 90000 + (income - 1200000) * 0.2
    else:
        return 150000 + (income - 1500000) * 0.3

ctc = float(input("Enter CTC: "))
bonus = float(input("Enter Bonus: "))
income = ctc + bonus
print(f"\nTotal Income: Rs.{income}")
old = old_regime_tax(income)
new = new_regime_tax(income)
print(f"Old Regime Tax: Rs.{old}")
print(f"New Regime Tax: Rs.{new}")
if old < new:
    print(f"You save Rs.{new - old} with Old Regime")
elif new < old:
    print(f"You save Rs.{old - new} with New Regime")
else:
    print("Both regimes give same tax.")
