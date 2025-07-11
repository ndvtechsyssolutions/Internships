def calculate_old_regime_tax(gross_income, hra_claimed, sec_80c=150000, std_deduction=50000):
    # Total deductions allowed under old regime
    total_deductions = std_deduction + sec_80c + hra_claimed
    taxable_income = gross_income - total_deductions
    tax = 0

    # Old regime tax slabs
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 1000000) * 0.30

    # Rebate under section 87A
    if taxable_income <= 500000:
        tax = 0

    return max(0, tax), max(0, taxable_income)


def calculate_new_regime_tax(income):
    tax = 0

    # New regime tax slabs
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = (300000 * 0.05) + (income - 600000) * 0.10
    elif income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (income - 1200000) * 0.20
    else:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (income - 1500000) * 0.30

    # Rebate under section 87A
    if income <= 700000:
        tax = 0

    return max(0, tax)


def main():
    print("=== Income Tax Calculator: Old vs New Regime ===")

    try:
        ctc = float(input("Enter your Annual CTC (₹): "))
        bonus = float(input("Enter your Annual Bonus (₹): "))
        hra = float(input("Enter your HRA claimed under Old Regime (₹): "))
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    # Step 1: Calculate gross income
    gross_income = ctc + bonus
    print(f"\nTotal Income including Bonus = ₹{gross_income:,.2f}")

    # Step 2: Calculate taxes under both regimes
    old_tax, old_taxable_income = calculate_old_regime_tax(gross_income, hra)
    new_tax = calculate_new_regime_tax(gross_income)

    # Step 3: Display comparison
    print("\n--- Tax Calculation Summary ---")
    print(f"Taxable Income under Old Regime: ₹{old_taxable_income:,.2f}")
    print(f"Tax under Old Regime: ₹{old_tax:,.2f}")
    print(f"Tax under New Regime: ₹{new_tax:,.2f}")

    print("\n--- Comparison Summary ---")
    if old_tax < new_tax:
        print("✅ Old Regime is better. You save more tax.")
    elif new_tax < old_tax:
        print("✅ New Regime is better. You save more tax.")
    else:
        print("⚖️ Both regimes result in the same tax.")

if __name__ == "__main__":
    main()
