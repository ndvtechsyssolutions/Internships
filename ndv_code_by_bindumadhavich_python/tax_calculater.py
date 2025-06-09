def calculate_old_regime_tax(income):
    """
    Calculates tax under the Old Regime
    considering standard deduction and 80C.
    """
    # Standard deduction
    std_deduction = 50000
    deduction_80c = 100000
    taxable_income = income - std_deduction - deduction_80c

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = taxable_income * 0.05
    elif taxable_income <= 1000000:
        tax =taxable_income * 0.20
    else:
        tax = taxable_income * 0.30

    return max(0, round(tax))


def calculate_new_regime_tax(income):

    """
    Calculates tax under the New Regime (FY 2024-25)
    No deductions allowed
    """
    income = income-50000
    tax = 0

    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = income * 0.05
    elif income <= 900000:
        tax =  income  * 0.10
    elif income <= 1200000:
        tax =  income  * 0.15
    elif income <= 1500000:
        tax = income * 0.20
    else:
        tax = income  * 0.30

    return round(tax)


def compare_regimes(ctc, bonus):
    """
    Compares the tax calculated using both regimes
    and suggests the better option.
    """
    total_income = ctc + bonus
    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"\nTotal Income: Rs.{total_income:,}")
    print(f"Old Regime Tax Deduction: Rs.{old_tax:,}")
    print(f"New Regime Tax Deduction: Rs.{new_tax:,}")

    if old_tax < new_tax:
        print(f"You Save Rs.{new_tax - old_tax:,} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"You Save Rs.{old_tax - new_tax:,} more using the New Regime.")
    else:
        print("Both regimes result in the same tax amount.")


def main_menu():
    """
    Displays the menu and handles user input.
    """
    while True:
        print("\n==== Income Tax Calculator (FY 2024-25) ====")
        print("1. Calculate Tax")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            try:
                ctc = float(input("Enter your CTC (in Rs): "))
                bonus = float(input("Enter your Bonus Amount (in Rs): "))
                compare_regimes(ctc, bonus)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '2':
            print("Thank you for using the Tax Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main_menu()
