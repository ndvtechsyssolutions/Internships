# tax_calculator.py

def calculate_old_regime_tax(income):
    """
    Calculates tax based on Old Regime with deductions:
    - Standard Deduction: ₹50,000
    - 80C Deduction: ₹1,50,000
    """
    deductions = 50000 + 150000
    taxable_income = max(0, income - deductions)
    tax = 0

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

    return tax


def calculate_new_regime_tax(income):
    """
    Calculates tax based on New Regime (no deductions)
    Slabs: FY 2024-25
    """
    slabs = [(300000, 0.0), (600000, 0.05), (900000, 0.10),
             (1200000, 0.15), (1500000, 0.20), (float('inf'), 0.30)]
    prev_limit = 0
    tax = 0

    for limit, rate in slabs:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            break

    return tax


def main():
    while True:
        print("\n--- Tax Deduction Calculator ---")
        try:
            ctc = float(input("Enter your Total CTC (in ₹): "))
            bonus = float(input("Enter your Bonus Amount (in ₹): "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        total_income = ctc + bonus
        print(f"\nTotal Income: ₹{total_income:,.2f}")

        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        print(f"\nOld Regime Tax Deduction: ₹{old_tax:,.2f}")
        print(f"New Regime Tax Deduction: ₹{new_tax:,.2f}")

        if old_tax < new_tax:
            print(f"\n✅ You Save ₹{new_tax - old_tax:,.2f} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"\n✅ You Save ₹{old_tax - new_tax:,.2f} more using the New Regime.")
        else:
            print("\nBoth regimes result in the same tax.")

        choice = input("\nDo you want to recalculate? (yes/no): ").lower()
        if choice != 'yes':
            print("Thank you for using the Tax Calculator!")
            break


if __name__ == "__main__":
    main()
