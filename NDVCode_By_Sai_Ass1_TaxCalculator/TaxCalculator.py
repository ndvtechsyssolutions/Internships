def calculate_old_regime_tax(income):
    # Apply standard deduction of ₹50,000
    income -= 50000

    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.20
    else:
        tax = 112500 + (income - 1000000) * 0.30

    return tax

def calculate_new_regime_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 750000:
        tax = 12500 + (income - 500000) * 0.10
    elif income <= 1000000:
        tax = 37500 + (income - 750000) * 0.15
    elif income <= 1250000:
        tax = 75000 + (income - 1000000) * 0.20
    elif income <= 1500000:
        tax = 125000 + (income - 1250000) * 0.25
    else:
        tax = 187500 + (income - 1500000) * 0.30

    return tax

def main():
    ctc = float(input("Enter Total CTC: "))
    bonus = float(input("Enter Total Bonus: "))

    total_income = ctc + bonus
    print(f"\nTotal Income (including bonus): ₹{total_income:.2f}")

    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"\nTax under Old Regime: ₹{old_tax:.2f}")
    print(f"Tax under New Regime: ₹{new_tax:.2f}")

    if old_tax < new_tax:
        print("\nRecommendation: Opt for the Old Regime.")
    elif new_tax < old_tax:
        print("\nRecommendation: Opt for the New Regime.")
    else:
        print("\nBoth regimes result in the same tax.")

if __name__ == "__main__":
    main()
