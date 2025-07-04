# Tax Deduction Calculator: Old vs New Regime
# Author: Rishika S
# Description: This console-based Python application calculates income tax
#              using both the Old and New Regime as per FY 2024-25 slabs.

# Function to calculate tax under the Old Regime
def calculate_old_regime_tax(income):
    # Fixed deductions under Old Regime
    standard_deduction = 50000
    section_80c_deduction = 150000
    total_deductions = standard_deduction + section_80c_deduction

    # Calculate taxable income after deductions
    taxable_income = max(0, income - total_deductions)
    tax = 0

    # Tax slabs for Old Regime:
    # 0–2.5L: 0%, 2.5L–5L: 5%, 5L–10L: 20%, above 10L: 30%

    if taxable_income > 1000000:
        tax += (taxable_income - 1000000) * 0.30
        taxable_income = 1000000
    if taxable_income > 500000:
        tax += (taxable_income - 500000) * 0.20
        taxable_income = 500000
    if taxable_income > 250000:
        tax += (taxable_income - 250000) * 0.05

    return tax

# Function to calculate tax under the New Regime
def calculate_new_regime_tax(income):
    tax = 0

    # New Regime Slabs:
    # 0–3L: 0%, 3L–6L: 5%, 6L–9L: 10%, 9L–12L: 15%, 12L–15L: 20%, 15L+: 30%
    slabs = [
        (300000, 0.00),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)  # Above 15L
    ]

    prev_limit = 0  # Tracks lower limit of current slab
    for limit, rate in slabs:
        if income > limit:
            tax += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            tax += (income - prev_limit) * rate
            break

    return tax

# Main function to interact with the user
def main():
    while True:
        try:
            # Get user input
            ctc = float(input("Enter your CTC: "))
            bonus = float(input("Enter your Bonus: "))
        except ValueError:
            print("❌ Please enter valid numeric values.")
            continue

        # Calculate total income
        total_income = ctc + bonus
        print(f"\n✅ Total Income: Rs.{total_income:.2f}")

        # Calculate tax for both regimes
        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        # Display tax results
        print(f"Old Regime Tax Deduction: Rs.{old_tax:.2f}")
        print(f"New Regime Tax Deduction: Rs.{new_tax:.2f}")

        # Suggest better regime
        if old_tax < new_tax:
            print(f"\n👉 You save Rs.{new_tax - old_tax:.2f} more using the Old Regime.")
        elif new_tax < old_tax:
            print(f"\n👉 You save Rs.{old_tax - new_tax:.2f} more using the New Regime.")
        else:
            print("\n👉 Both regimes result in the same tax amount.")

        # Option to recalculate or exit
        option = input("\nDo you want to calculate again? (y/n): ")
        if option.lower() != 'y':
            print("✅ Thank you for using the Tax Calculator. Goodbye!")
            break

# Entry point of the program
if __name__ == "__main__":
    main()
