#Tax calculation based on old and new regime and suggesting using which regime the user saves more

#old regime tax calculation
def calculate_old_regime_tax(income):
    standard_deduction = 50000
    section_80c_deduction = 150000
    hra = 40000

    # Total deductions
    total_deductions = standard_deduction + section_80c_deduction + hra

    # Taxable income under old regime
    taxable_income = max(0, income - total_deductions)

    tax = 0
    
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.3

    return int(tax)

#new regime tax calculation
def calculate_new_regime_tax(income):
    tax = 0
    
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = 15000 + (income - 600000) * 0.1
    elif income <= 1200000:
        tax = 45000 + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = 90000 + (income - 1200000) * 0.2
    else:
        tax = 150000 + (income - 1500000) * 0.3

    return int(tax)

#Main function
def tax_calculator_menu():
    while True:
        print("\n--- Tax Calculator: Old vs New Regime ---")
        try:
            ctc = float(input("Enter your CTC (Annual Salary): Rs. "))
            bonus = float(input("Enter your Annual Bonus: Rs. "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        total_income = ctc + bonus
        print(f"\nTotal Income (CTC + Bonus): Rs. {int(total_income)}")

        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        print(f"\nOld Regime Tax: Rs. {old_tax}")
        print(f"New Regime Tax: Rs. {new_tax}")

        # Suggesting the better regime
        if old_tax < new_tax:
            print(f"\nYou save Rs. {new_tax - old_tax} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"\nYou save Rs.{old_tax - new_tax} more using the New Regime.")
        else:
            print("\nBoth regime results in same tax for your entered CTC and bonus amount.")

        # Menu options
        print("\n1. Recalculate")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")
        if choice != '1':
            print("Thank You For using Tax Calculator.")
            break

tax_calculator_menu()
