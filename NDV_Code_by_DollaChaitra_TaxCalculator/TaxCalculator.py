def calculate_old_regime_tax(total_income):
    """
    Calculates tax as per the Old Tax Regime
    Standard Deduction = ₹50,000
    80C Deduction = ₹1,50,000
    """
    std_deduction = 50000
    section_80C = 150000
    taxable_income = total_income - std_deduction - section_80C

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = 0.05 * (taxable_income - 250000)
    elif taxable_income <= 1000000:
        tax = 12500 + 0.2 * (taxable_income - 500000)
    else:
        tax = 112500 + 0.3 * (taxable_income - 1000000)

    return max(tax, 0)


def calculate_new_regime_tax(total_income):
    """
    Calculates tax as per the New Tax Regime (FY 2024-25 slabs)
    No deductions allowed
    """
    slabs = [(300000, 0.0), (600000, 0.05), (900000, 0.10),
             (1200000, 0.15), (1500000, 0.20), (float('inf'), 0.30)]
    prev_limit = 0
    tax = 0.0

    for limit, rate in slabs:
        if total_income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (total_income - prev_limit) * rate
            break

    return max(tax, 0)


def show_summary(ctc, bonus):
    total_income = ctc + bonus
    print(f"\nTotal Income: ₹{total_income:,}")

    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"Old Regime Tax Deduction: ₹{old_tax:,.2f}")
    print(f"New Regime Tax Deduction: ₹{new_tax:,.2f}")

    if old_tax < new_tax:
        print(f"\nYou Save ₹{new_tax - old_tax:,.2f} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"\nYou Save ₹{old_tax - new_tax:,.2f} more using the New Regime.")
    else:
        print("\nBoth regimes result in the same tax amount.")


def main():
    print("----- Tax Calculator: Old vs New Regime (FY 2024-25) -----")
    while True:
        try:
            ctc = float(input("Enter your CTC (in ₹): "))
            bonus = float(input("Enter your Bonus (in ₹): "))
            show_summary(ctc, bonus)
        except ValueError:
            print("Please enter valid numeric values for CTC and Bonus.")
            continue

        print("\nMenu:\n1. Recalculate\n2. Exit")
        choice = input("Choose an option: ")
        if choice != '1':
            print("Thank you for using the Tax Calculator.")
            break


if __name__ == "__main__":
    main()
