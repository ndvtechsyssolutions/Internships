def calculate_tax_old_regime(income):
    standard_deduction = 50000
    deduction_80C = 150000
    taxable = income - standard_deduction - deduction_80C

    if taxable <= 250000:
        return 0
    elif taxable <= 500000:
        return (taxable - 250000) * 0.05
    elif taxable <= 1000000:
        return (250000 * 0.05) + (taxable - 500000) * 0.2
    else:
        return (250000 * 0.05) + (500000 * 0.2) + (taxable - 1000000) * 0.3


def calculate_tax_new_regime(income):
    brackets = [
        (300000, 0.00),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30)
    ]

    tax = 0
    for limit, rate in brackets:
        if income > limit:
            tax += limit * rate
            income -= limit
        else:
            tax += income * rate
            break
    return tax


def tax_summary(income, bonus):
    total = income + bonus
    old_tax = calculate_tax_old_regime(total)
    new_tax = calculate_tax_new_regime(total)

    print(f"\nNet Income: ₹{int(total)}")
    print(f"Old Regime Tax: ₹{int(old_tax)}")
    print(f"New Regime Tax: ₹{int(new_tax)}")

    if old_tax < new_tax:
        print(f"→ Save ₹{int(new_tax - old_tax)} using Old Regime")
    elif new_tax < old_tax:
        print(f"→ Save ₹{int(old_tax - new_tax)} using New Regime")
    else:
        print("→ No difference in tax between both regimes")


def run_tax_calculator():
    while True:
        print("\n========== Tax Regime Comparison ==========")
        try:
            base = float(input("Enter your Base Salary: ₹"))
            add = float(input("Enter your Bonus/Other Income: ₹"))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        tax_summary(base, add)

        repeat = input("\nDo you want to run another calculation? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Exiting. Have a great day!")
            break


if __name__ == "__main__":
    run_tax_calculator()
