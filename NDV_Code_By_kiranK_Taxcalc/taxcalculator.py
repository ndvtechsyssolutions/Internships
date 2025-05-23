def calculate_old_regime_tax(income):
    deductions = 50000 + 150000  
    taxable_income = max(0, income - deductions)

    if taxable_income <= 250000:
        return 0
    elif taxable_income <= 500000:
        return (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        return 12500 + (taxable_income - 500000) * 0.2
    else:
        return 112500 + (taxable_income - 1000000) * 0.3


def calculate_new_regime_tax(income):
    if income <= 300000:
        return 0
    elif income <= 600000:
        return (income - 300000) * 0.05
    elif income <= 900000:
        return 15000 + (income - 600000) * 0.1
    elif income <= 1200000:
        return 45000 + (income - 900000) * 0.15
    elif income <= 1500000:
        return 90000 + (income - 1200000) * 0.2
    else:
        return 150000 + (income - 1500000) * 0.3


def display_tax_summary(income, old_tax, new_tax):
    print("\n📊 Tax Summary")
    print(f"💰 Total Income: ₹{income:,}")
    print(f"🏛️ Old Regime Tax: ₹{old_tax:,.2f}")
    print(f"🏛️ New Regime Tax: ₹{new_tax:,.2f}")

    if old_tax < new_tax:
        print(f"✅ You save ₹{new_tax - old_tax:,.2f} with the Old Tax Regime.")
    elif new_tax < old_tax:
        print(f"✅ You save ₹{old_tax - new_tax:,.2f} with the New Tax Regime.")
    else:
        print("⚖️ Both regimes result in the same tax amount.")

    print("✅ Calculation Complete. Thank you!")


def main():
    try:
        ctc = int(input("Enter your Annual CTC (₹): "))
        bonus = int(input("Enter your Annual Bonus (₹): "))
        total_income = ctc + bonus

        old_tax = calculate_old_regime_tax(total_income)
        new_tax = calculate_new_regime_tax(total_income)

        display_tax_summary(total_income, old_tax, new_tax)

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
