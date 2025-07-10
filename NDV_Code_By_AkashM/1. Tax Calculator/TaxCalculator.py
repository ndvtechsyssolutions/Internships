def old_regime_tax(income):
    std_deduction = 50000
    hra = 50000
    deduction_80C = 150000
    taxable = income - std_deduction - hra - deduction_80C

    tax = 0
    if taxable <= 250000:
        tax = 0
    elif taxable <= 500000:
        tax = (taxable - 250000) * 0.05
    elif taxable <= 1000000:
        tax = 12500 + (taxable - 500000) * 0.2
    else:
        tax = 112500 + (taxable - 1000000) * 0.3
    return tax


def new_regime_tax(income):
    slabs = [(300000, 0), (600000, 0.05), (900000, 0.1), (1200000, 0.15), (1500000, 0.2)]
    tax = 0
    prev_limit = 0

    for limit, rate in slabs:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            return tax

    tax += (income - 1500000) * 0.3
    return tax


def main():
    ctc = float(input("Enter your Total CTC: ₹"))
    bonus = float(input("Enter your Bonus Amount: ₹"))
    total_income = ctc + bonus

    print("\n--- Income Details ---")
    print(f"Total Income (CTC + Bonus): ₹{total_income}")

    old_tax = old_regime_tax(total_income)
    new_tax = new_regime_tax(total_income)

    print("\n--- Tax Comparison ---")
    print(f"Old Regime Tax: ₹{old_tax}")
    print(f"New Regime Tax: ₹{new_tax}")
    ans = 0
    if old_tax < new_tax:
        ans = new_tax - old_tax
        print(f"You save Rs.{ans} more using the Old Regime")
    elif old_tax > new_tax:
        ans = old_tax - new_tax
        print(f"You save Rs.{ans} more using the New Regime")
    else:
        print("Both regimes result in the same tax amount.")


if __name__ == "__main__":
    main()