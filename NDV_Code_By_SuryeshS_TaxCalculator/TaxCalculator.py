def calculate_old_regime_tax(income):
    """
    Calculates income tax under the OLD regime for FY 2024–25.
    
    ▶ Deductions Allowed:
      - Standard Deduction: ₹50,000
      - Section 80C: ₹1,50,000
      → Total Deductions: ₹2,00,000

    ▶ Taxable Income = Total Income - Deductions
      - For example, if your total income is ₹6,50,000
        Then: ₹6,50,000 - ₹2,00,000 = ₹4,50,000 (taxable income)

    ▶ Section 87A Rebate:
      - If your taxable income is ≤ ₹5,00,000, you get a rebate of up to ₹12,500.
      - This rebate is subtracted from the calculated tax.
      - It reduces your final tax to ₹0 (not just reduced — fully waived).
    """

    # Step 1: Apply deductions
    standard_deduction = 50000
    deduction_80c = 150000
    taxable_income = income - standard_deduction - deduction_80c

    if taxable_income <= 0:
        return 0  # No tax if taxable income is zero or negative

    # Step 2: Apply old tax slabs
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3

    # Step 3: Apply 87A rebate if income is ≤ ₹5L
    if taxable_income <= 500000:
        tax = max(0, tax - 12500)

    # Step 4: Add 4% Health & Education Cess
    tax += tax * 0.04

    return int(tax)


def calculate_new_regime_tax(income):
    """
    Calculates income tax under the NEW regime for FY 2024–25.

    ▶ Deductions Allowed:
      - Standard Deduction (salary/pension only): ₹75,000
      - No 80C, 80D, HRA, LTA, etc.

    ▶ Taxable Income = Total Income - ₹75,000
      - For example: ₹6,50,000 - ₹75,000 = ₹5,75,000

    ▶ Section 87A Rebate:
      - If taxable income ≤ ₹7,00,000, you get full rebate of up to ₹25,000
      - This makes your final tax = ₹0
    """

    # Step 1: Apply standard deduction (only one allowed in new regime)
    standard_deduction = 75000
    taxable_income = income - standard_deduction

    if taxable_income <= 0:
        return 0

    # Step 2: Apply new tax slabs
    tax = 0
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = (300000 * 0.05) + (taxable_income - 600000) * 0.1
    elif taxable_income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.1) + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = (
            300000 * 0.05 +
            300000 * 0.1 +
            300000 * 0.15 +
            (taxable_income - 1200000) * 0.2
        )
    else:
        tax = (
            300000 * 0.05 +
            300000 * 0.1 +
            300000 * 0.15 +
            300000 * 0.2 +
            (taxable_income - 1500000) * 0.3
        )

    # Step 3: Apply 87A rebate if taxable income ≤ ₹7L
    # Example: if income is ₹6,50,000 - 75,000 = ₹5,75,000 → eligible
    if taxable_income <= 700000:
        tax = max(0, tax - 25000)

    # Step 4: Add 4% Health & Education Cess
    tax += tax * 0.04

    return int(tax)


def start_tax_calculator():
    """
    This function interacts with the user:
    - Takes CTC and Bonus
    - Computes tax under both regimes
    - Compares which regime is better
    - Allows repeated calculations
    """
    while True:
        try:
            ctc = float(input("Enter your CTC: "))
            bonus = float(input("Enter your Bonus: "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

        total_income = ctc + bonus
        print(f"\nTotal Income: Rs.{int(total_income)}")

        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        print(f"Old Regime Tax Deduction: Rs.{old_tax}")
        print(f"New Regime Tax Deduction: Rs.{new_tax}")

        if old_tax < new_tax:
            print(f"You Save Rs.{new_tax - old_tax} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"You Save Rs.{old_tax - new_tax} more using the New Regime.")
        else:
            print("Both regimes result in the same tax amount.")

        choice = input("\nDo you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("Thank you for using the Tax Calculator.")
            break


if __name__ == "__main__":
    start_tax_calculator()
