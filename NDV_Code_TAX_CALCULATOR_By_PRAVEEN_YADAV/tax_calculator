def calculate_old_regime_tax(income):
    standard_deduction = 50000
    deduction_80C = 150000

    taxable_income = max(income - standard_deduction - deduction_80C, 0)
    return calculate_tax_old_regime(taxable_income)


def calculate_new_regime_tax(income):
    return calculate_tax_new_regime(income)


def calculate_tax_old_regime(taxable_income):
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


def calculate_tax_new_regime(taxable_income):
    tax = 0
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = 15000 + (taxable_income - 600000) * 0.1
    elif taxable_income <= 1200000:
        tax = 45000 + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = 90000 + (taxable_income - 1200000) * 0.2
    else:
        tax = 150000 + (taxable_income - 1500000) * 0.3
    return tax


def display_summary(ctc, bonus):
    total_income = ctc + bonus
    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"\nTotal Income: Rs.{total_income:,}")
    print(f"Old Regime Tax Deduction: Rs.{old_tax:,.2f}")
    print(f"New Regime Tax Deduction: Rs.{new_tax:,.2f}")

    if old_tax < new_tax:
        print(f"\nYou Save Rs.{new_tax - old_tax:,.2f} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"\nYou Save Rs.{old_tax - new_tax:,.2f} more using the New Regime.")
    else:
        print("\nBoth regimes result in the same tax amount.")


def main_menu():
    while True:
        print("\n==== Tax Calculator Menu ====")
        print("1. Calculate Tax")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            try:
                ctc = float(input("Enter your CTC: "))
                bonus = float(input("Enter your Bonus: "))
                display_summary(ctc, bonus)
            except ValueError:
                print("Invalid input. Please enter numerical values.")
        elif choice == '2':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main_menu()
