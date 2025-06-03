# tax_calculator.py
# Author: B. Hemanth Kumar
# Description: Console-based Tax Calculator for Old vs New Regime

def calculate_old_regime_tax(income):
    standard_deduction = 50000
    deduction_80C = 150000
    taxable_income = max(0, income - standard_deduction - deduction_80C)

    # Old tax slabs (FY 2024–25)
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.3

    return tax


def calculate_new_regime_tax(income):
    # New tax slabs (FY 2024–25)
    tax = 0
    slabs = [
        (300000, 0),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (300000, 0.25),
        (float('inf'), 0.30)
    ]

    remaining_income = income
    for slab_limit, rate in slabs:
        slab_taxable = min(remaining_income, slab_limit)
        tax += slab_taxable * rate
        remaining_income -= slab_taxable
        if remaining_income <= 0:
            break

    return tax


def display_summary(ctc, bonus):
    total_income = ctc + bonus
    print(f"\nTotal Income: Rs.{total_income}")

    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"Old Regime Tax Deduction: Rs.{old_tax:,.2f}")
    print(f"New Regime Tax Deduction: Rs.{new_tax:,.2f}")

    if old_tax < new_tax:
        print(f"You Save Rs.{new_tax - old_tax:,.2f} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"You Save Rs.{old_tax - new_tax:,.2f} more using the New Regime.")
    else:
        print("Both regimes result in the same tax amount.")


def main():
    while True:
        try:
            ctc = float(input("\nEnter your CTC: "))
            bonus = float(input("Enter your Bonus: "))
            display_summary(ctc, bonus)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        print("\n1. Recalculate\n2. Exit")
        choice = input("Choose an option: ")
        if choice == '2':
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
