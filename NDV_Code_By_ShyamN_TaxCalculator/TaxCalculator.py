def old_tax(income):
    std_deduction = 50000
    deduction_80c = 150000
    taxable = max(income - std_deduction - deduction_80c, 0)

    if taxable <= 250000:
        return 0
    elif taxable <= 500000:
        return 0.05 * (taxable - 250000)
    elif taxable <= 1000000:
        return 12500 + 0.20 * (taxable - 500000)
    else:
        return 112500 + 0.30 * (taxable - 1000000)


def new_tax(income):
    if income <= 300000:
        return 0
    elif income <= 600000:
        return 0.05 * (income - 300000)
    elif income <= 900000:
        return 15000 + 0.10 * (income - 600000)
    elif income <= 1200000:
        return 45000 + 0.15 * (income - 900000)
    elif income <= 1500000:
        return 90000 + 0.20 * (income - 1200000)
    else:
        return 150000 + 0.30 * (income - 1500000)


def compare(ctc, bonus):
    total = ctc + bonus
    print(f"\nTotal Income: Rs.{total:,.2f}")

    tax_old = old_tax(total)
    tax_new = new_tax(total)

    print(f"Old Regime Tax Deduction: Rs.{tax_old:,.2f}")
    print(f"New Regime Tax Deduction: Rs.{tax_new:,.2f}")

    diff = abs(tax_old - tax_new)
    if tax_old < tax_new:
        print(f"\nYou Save Rs.{diff:,.2f} more using the Old Regime.")
    elif tax_new < tax_old:
        print(f"\nYou Save Rs.{diff:,.2f} more using the New Regime.")
    else:
        print("\nBoth regimes cost you the same in tax.")


def run():
    while True:
        print("\n- Tax Calculator -")
        print("1. Calculate Tax")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            try:
                ctc = float(input("Enter your Total CTC (Rs): "))
                bonus = float(input("Enter your Bonus Amount (Rs): "))
                compare(ctc, bonus)
            except:
                print("Please enter valid numbers.")
        elif choice == '2':
            print("Exit successful")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    run()
