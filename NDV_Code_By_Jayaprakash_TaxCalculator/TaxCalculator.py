def calculate_old_regime_tax(income):

    standard_deduction = 50000
    deduction_80C = 150000
    taxable_income = max(income - standard_deduction - deduction_80C, 0)

    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = 0.05 * (taxable_income)
    elif taxable_income <= 1000000:
        tax = 0.2 * (taxable_income)
    else:
        tax = 0.3 * (taxable_income)

    return round(tax)


def calculate_new_regime_tax(income):
    """
    Calculates tax as per New Tax Regime (No deductions).
    Slabs: 0–3L: 0%, 3–6L: 5%, 6–9L: 10%, 9–12L: 15%, 12–15L: 20%, 15L+: 30%
    """
    slabs = [300000, 600000, 900000, 1200000, 1500000]
    rates = [0.05, 0.1, 0.15, 0.2, 0.3]

    tax = 0
    prev_limit = 0
    for i in range(len(slabs)):
        if income > slabs[i]:
            tax += (slabs[i] - prev_limit) * rates[i]
            prev_limit = slabs[i]
        else:
            tax += (income - prev_limit) * rates[i]
            return round(tax)

    tax += (income - slabs[-1]) * 0.3
    return round(tax)


def compare_regimes(ctc, bonus):
    total_income = ctc + bonus
    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"\nTotal Income: ₹{total_income}")
    print(f"Old Regime Tax Deduction: ₹{old_tax}")
    print(f"New Regime Tax Deduction: ₹{new_tax}")

    if old_tax < new_tax:
        savings = new_tax - old_tax
        print(f"You save ₹{savings} more using the Old Regime.")
    elif new_tax < old_tax:
        savings = old_tax - new_tax
        print(f"You save ₹{savings} more using the New Regime.")
    else:
        print("Both regimes result in the same tax. Choose either.")


def main():
    while True:
        print("\n--- Tax Calculator Menu ---")
        print("1. Calculate Tax")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ").strip()
        if choice == '1':
            try:
                ctc = int(input("Enter your CTC (₹): "))
                bonus = int(input("Enter your Bonus (₹): "))
                compare_regimes(ctc, bonus)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == '2':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
