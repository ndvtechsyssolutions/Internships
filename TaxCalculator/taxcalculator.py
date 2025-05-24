# Tax Deduction Calculator - Old vs New Regime
# Author: Nihal Mishra
# Date: May 2025

# Function to calculate tax using Old Regime
def old_regime_tax(income):
    # Deduct standard deduction and 80C
    standard_deduction = 50000
    deduction_80C = 150000
    taxable_income = income - standard_deduction - deduction_80C

    if taxable_income <= 0:
        return 0

    tax = 0
    # Apply old regime slab rates
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

    return round(tax)

# Function to calculate tax using New Regime
def new_regime_tax(income):
    tax = 0

    # New regime slabs (FY 2024-25)
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.10
    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (income - 1200000) * 0.20
    else:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (income - 1500000) * 0.30

    return round(tax)

# Main function to run the calculator
def tax_calculator():
    while True:
        print("\n--- Welcome to Tax Calculator ---")
        try:
            ctc = int(input("Enter your Total CTC (in ₹): "))
            bonus = int(input("Enter your Bonus (in ₹): "))
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        total_income = ctc + bonus
        old_tax = old_regime_tax(total_income)
        new_tax = new_regime_tax(total_income)

        print("\n--- Tax Calculation Summary ---")
        print(f"Total Income: ₹{total_income}")
        print(f"Old Regime Tax: ₹{old_tax}")
        print(f"New Regime Tax: ₹{new_tax}")

        # Suggest better option
        if old_tax < new_tax:
            print(f"✅ You save ₹{new_tax - old_tax} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"✅ You save ₹{old_tax - new_tax} more using the New Regime.")
        else:
            print("✅ Both regimes result in the same tax.")

        # Menu to recalculate or exit
        print("\nDo you want to:")
        print("1. Recalculate")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice != '1':
            print("👋 Exiting Tax Calculator. Thank you!")
            break

# Run the calculator
tax_calculator()
