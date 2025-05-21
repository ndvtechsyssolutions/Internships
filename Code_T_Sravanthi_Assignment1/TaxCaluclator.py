# Constants for deductions (Old Regime)
STANDARD_DEDUCTION = 50000
SECTION_80C_LIMIT = 150000
HRA_EXEMPTION = 200000  # simplified fixed value
# Tax slabs: (lower_limit, upper_limit, tax_rate)
OLD_REGIME_SLABS = [
    (0, 250000, 0.0),
    (250000, 500000, 0.05),
    (500000, 1000000, 0.20),
    (1000000, float('inf'), 0.30)
]
NEW_REGIME_SLABS = [
    (0, 300000, 0.0),
    (300000, 600000, 0.05),
    (600000, 900000, 0.10),
    (900000, 1200000, 0.15),
    (1200000, 1500000, 0.20),
    (1500000, float('inf'), 0.30)
]
def calculate_tax(income, slabs):
    """Calculate tax for given income and tax slabs."""
    tax = 0
    for lower, upper, rate in slabs:
        if income > lower:
            taxable = min(income, upper) - lower
            tax += taxable * rate
        else:
            break
    return round(tax)
def calculate_old_regime_tax(income):
    """Calculate old regime tax considering fixed deductions."""
    deductions = STANDARD_DEDUCTION + SECTION_80C_LIMIT + HRA_EXEMPTION
    taxable_income = max(income - deductions, 0)
    return calculate_tax(taxable_income, OLD_REGIME_SLABS)
def calculate_new_regime_tax(income):
    """Calculate new regime tax without deductions."""
    return calculate_tax(income, NEW_REGIME_SLABS)
def get_float_input(prompt):
    """Get valid float input from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
def main():
    while True:
        ctc = get_float_input("Enter your CTC : ")
        bonus = get_float_input("Enter your Bonus:")
        total_income = ctc + bonus
        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)
        savings = new_tax - old_tax
        print(f"Total income:Rs.{total_income},")
        print(f"Old Regime tax deduction:Rs.{old_tax},")
        print(f"New Regime tax deduction:Rs.{new_tax},")
        if savings > 0:
            print(f"You save rs.{savings} more using the old")
        elif savings < 0:
            print(f"You save rs.{-savings} more using the new")
        else:
            print("Both regimes result in the same tax")
        # Option to continue or exit
        choice = input("\nDo you want to recalculate? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you")
            break
if __name__ == "__main__":
    main()
