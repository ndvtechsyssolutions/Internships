def calculate_old_regime_tax(total_income):
    standard_deduction = 50000
    deduction_80C = 150000
    total_deductions = standard_deduction + deduction_80C

    taxable_income = total_income - total_deductions
    if taxable_income <= 0:
        return 0

    
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 1000000) * 0.30

    if taxable_income <= 500000:
        tax = 0

    return round(tax, 2)


def calculate_new_regime_tax(total_income):
    
    slabs = [0, 300000, 600000, 900000, 1200000, 1500000]
    rates = [0, 0.05, 0.10, 0.15, 0.20, 0.30]

    tax = 0
    for i in range(1, len(slabs)):
        lower = slabs[i - 1]
        upper = slabs[i]
        if total_income > lower:
            tax += (min(total_income, upper) - lower) * rates[i]
        else:
            break

    if total_income > 1500000:
        tax += (total_income - 1500000) * 0.30

    
    if total_income <= 700000:
        tax = 0

    return round(tax, 2)


def show_summary(ctc, bonus):
    
    total_income = ctc + bonus
    print(f"\nTotal Income: ₹{total_income:,.2f}")

    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print(f"Old Regime Tax Deduction: ₹{old_tax:,.2f}")
    print(f"New Regime Tax Deduction: ₹{new_tax:,.2f}")

    if old_tax < new_tax:
        print(f"\n You Save ₹{new_tax - old_tax:,.2f} more using the Old Regime.")
    elif new_tax < old_tax:
        print(f"\n You Save ₹{old_tax - new_tax:,.2f} more using the New Regime.")
    else:
        print("\nBoth regimes result in the same tax.")


def main():
    ctc = float(input("\nEnter your annual CTC (₹): "))
    bonus = float(input("Enter your Bonus amount (₹): "))
    show_summary(ctc, bonus)
 
if __name__ == "__main__":
    main()
