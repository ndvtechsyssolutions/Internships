def old_regime_tax(income):
    income -= 50000  # Standard Deduction
    income -= 150000  # 80C Deduction

    if income <= 250000:
        return 0
    elif income <= 500000:
        return 0.05 * (income - 250000)
    elif income <= 1000000:
        return 12500 + 0.2 * (income - 500000)
    else:
        return 12500 + 100000 + 0.3 * (income - 1000000)

def new_regime_tax(income):
    if income <= 250000:
        return 0
    elif income <= 500000:
        return 0.05 * (income - 250000)
    elif income <= 750000:
        return 12500 + 0.1 * (income - 500000)
    elif income <= 1000000:
        return 12500 + 25000 + 0.15 * (income - 750000)
    elif income <= 1250000:
        return 12500 + 25000 + 37500 + 0.2 * (income - 1000000)
    elif income <= 1500000:
        return 12500 + 25000 + 37500 + 50000 + 0.25 * (income - 1250000)
    else:
        return 12500 + 25000 + 37500 + 50000 + 62500 + 0.3 * (income - 1500000)

def main():
    print("Tax Calculator - Financial Year 2024-25")
    try:
        ctc = float(input("Enter your Total CTC (₹): "))
        bonus = float(input("Enter your Bonus (₹): "))
        total_income = ctc + bonus

        old_tax = int(old_regime_tax(total_income))
        new_tax = int(new_regime_tax(total_income))

        print(f"\nTotal Income: ₹{total_income:,.0f}")
        print(f"Old Regime Tax: ₹{old_tax:,}")
        print(f"New Regime Tax: ₹{new_tax:,}")

        if old_tax < new_tax:
            print(f"Old Regime saves you ₹{new_tax - old_tax:,}")
        elif new_tax < old_tax:
            print(f"New Regime saves you ₹{old_tax - new_tax:,}")
        else:
            print("Both regimes result in the same tax.")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
