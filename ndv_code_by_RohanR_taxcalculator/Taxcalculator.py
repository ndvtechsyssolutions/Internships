def calculate_old_regime_tax(income):
    # Apply deductions
    standard_deduction = 50000
    section_80c_deduction = 150000
    taxable_income = max(0, income - standard_deduction - section_80c_deduction)

    tax = 0

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 1000000) * 0.30

    return round(tax)


def calculate_new_regime_tax(income):
    tax = 0
    slabs = [
        (300000, 0.0),
        (300000, 0.05),
        (300000, 0.10),
        (300000, 0.15),
        (300000, 0.20),
        (float('inf'), 0.30),
    ]

    remaining_income = income
    for slab_limit, rate in slabs:
        if remaining_income <= 0:
            break
        taxable = min(remaining_income, slab_limit)
        tax += taxable * rate
        remaining_income -= taxable

    return round(tax)


def show_summary(ctc, bonus):
    total_income = ctc + bonus
    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"\nTotal Income: Rs.{total_income}")
    print(f"Old Regime Tax Deduction: Rs.{old_tax}")
    print(f"New Regime Tax Deduction: Rs.{new_tax}")

    if old_tax < new_tax:
        print(f"\nYou Save Rs.{new_tax - old_tax} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"\nYou Save Rs.{old_tax - new_tax} more using the New Regime.")
    else:
        print("\nBoth regimes result in the same tax amount.")


def main_menu():
    while True:
        print("\n--- Tax Deduction Calculator ---")

        ctc = int(input("Enter your CTC: "))
        bonus = int(input("Enter your Bonus: "))

        show_summary(ctc, bonus)

        print("\nOptions:")
        print("1. Recalculate")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice != "1":
            print("Thank you for using the Tax Calculator.")
            break


if __name__ == "__main__":
    main_menu()
