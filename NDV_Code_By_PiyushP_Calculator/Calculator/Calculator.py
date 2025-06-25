def calculate_old_regime_tax(income):
    STANDARD_DEDUCTION = 50000
    DEDUCTION_80C = 150000
    taxable_income = income - STANDARD_DEDUCTION - DEDUCTION_80C

    if taxable_income <= 0:
        return 0
    elif taxable_income <= 250000:
        return 0
    elif taxable_income <= 500000:
        return 0.05 * (taxable_income - 250000)
    elif taxable_income <= 1000000:
        return (0.05 * 250000 + 0.2 * (taxable_income - 500000))
    else:
        return (0.05 * 250000 + 0.2 * 500000 + 0.3 * (taxable_income - 1000000))

def calculate_new_regime_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return 0.05 * (income - 250000)
    elif income <= 750000:
        return (0.05 * 250000 + 0.1 * (income - 500000))
    elif income <= 1000000:
        return (0.05 * 250000 + 0.1 * 250000 + 0.15 * (income - 750000))
    elif income <= 1250000:
        return (0.05 * 250000 + 0.1 * 250000 + 0.15 * 250000 + 0.2 * (income - 1000000))
    elif income <= 1500000:
        return (0.05 * 250000 + 0.1 * 250000 + 0.15 * 250000 + 0.2 * 250000 + 0.25 * (income - 1250000))
    else:
        return (0.05 * 250000 + 0.1 * 250000 + 0.15 * 250000 + 0.2 * 250000 + 0.25 * 250000 + 0.3 * (income - 1500000))


def show_summary(ctc, bonus):
    total_income = ctc + bonus
    print(f"\nTotal Income (CTC + Bonus): ₹{total_income:,}")

    old_tax = int(calculate_old_regime_tax(total_income))
    new_tax = int(calculate_new_regime_tax(total_income))

    print(f"\nOld Regime Tax Deduction: ₹{old_tax:,}")
    print(f"New Regime Tax Deduction: ₹{new_tax:,}")

    if old_tax < new_tax:
        print(f"\n You have Save ₹{new_tax - old_tax:,} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"\n You have Save ₹{old_tax - new_tax:,} more using the New Regime.")
    else:
        print("\n Both regimes are result in the same tax amount.")


def main():
    print("Welcome to the Tax Deduction Calculator - FY 2024-25")
    while True:
        try:
            ctc = int(input("\nEnter your Total CTC: "))
            bonus = int(input("Enter your Total Bonus: "))
            show_summary(ctc, bonus)
        except ValueError:
            print(" Please enter valid numeric values.")
            continue

        print("\nMenu:")
        print("1. Recalculate")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")
        if choice == '2':
            print("Thank you for using the Tax Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()


