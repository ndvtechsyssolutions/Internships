def old_tax_regime(income):
    std_deduction = 50000
    income -= std_deduction
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3
    if income <= 500000:
        tax = 0
    return tax

def new_tax_regime(income):
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.1
    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (income - 1200000) * 0.2
    else:
        tax = (300000 * 0.05) + (300000 * 0.1) + (300000 * 0.15) + (300000 * 0.2) + (income - 1500000) * 0.3
    if income <= 700000:
        tax = 0
    return tax

def display_summary(name, income, regime, tax):
    print("\n--- Tax Summary ---")
    print(f"Name: {name}")
    print(f"Annual Income: ₹{income:,.2f}")
    print(f"Tax Regime: {regime}")
    print(f"Calculated Tax: ₹{tax:,.2f}")

while True:
    name = input("Enter your name: ")
    income = float(input("Enter your annual income in INR: "))
    regime = input("Choose tax regime (old/new): ").strip().lower()
    
    if regime == 'old':
        tax = old_tax_regime(income)
    elif regime == 'new':
        tax = new_tax_regime(income)
    else:
        print("Invalid regime. Please enter 'old' or 'new'.")
        continue

    display_summary(name, income, regime, tax)

    again = input("Do you want to calculate tax for another person? (yes/no): ").strip().lower()
    if again != 'yes':
        break
