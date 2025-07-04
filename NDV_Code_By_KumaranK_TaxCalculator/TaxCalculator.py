def calculate_old_regime_tax(income):
    standard_deduction = 50000
    section_80C_deduction = 150000

    taxable_income = max(income - standard_deduction - section_80C_deduction, 0)

    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

    return round(tax, 2)


def calculate_new_regime_tax(income):
    tax = 0
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

    return round(tax, 2)


def main():
    while True:
        print("\n--- Tax Deduction Calculator ---")
        try:
            ctc = float(input("Enter your Total CTC (Rs.): "))
            bonus = float(input("Enter your Bonus (Rs.): "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        total_income = ctc + bonus
        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        print(f"\nTotal Income: Rs.{total_income:,.2f}")
        print(f"Old Regime Tax Deduction: Rs.{old_tax:,.2f}")
        print(f"New Regime Tax Deduction: Rs.{new_tax:,.2f}")

        if old_tax < new_tax:
            print(f"You save Rs.{new_tax - old_tax:,.2f} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"You save Rs.{old_tax - new_tax:,.2f} more using the New Regime.")
        else:
            print("Both regimes yield the same tax. Choose based on other deductions.")

        choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
