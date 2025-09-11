def calculate_tax(income):
    """
    Income Tax Calculator - India (Old Regime Slabs)
    Slabs:
    - Up to ₹2.5L: 0%
    - ₹2.5L to ₹5L: 5%
    - ₹5L to ₹10L: 20%
    - Above ₹10L: 30%
    """

    if income <= 250000:
        return 0
    elif income <= 500000:
        return (income - 250000) * 0.05
    elif income <= 1000000:
        return (250000 * 0.05) + (income - 500000) * 0.20
    else:
        return (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

def main():
    print("💰 Income Tax Calculator - India 🇮🇳")
    try:
        income = float(input("Enter your annual income (₹): "))
        tax = calculate_tax(income)
        print(f"Your estimated tax is: ₹{tax:,.2f}")
    except ValueError:
        print("🚫 Please enter a valid number!")

if __name__ == "__main__":
    main()
