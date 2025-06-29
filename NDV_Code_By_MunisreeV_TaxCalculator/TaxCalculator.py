#calculating old regime
def old_regime_tax(income):
    standard_deduction = 50000
    deduction_80C = 150000
    taxable_income = max(0, income - standard_deduction - deduction_80C)
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.3

    return round(tax)
#calculating new regime
def new_regime_tax(income):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 750000:
        tax = 12500 + (income - 500000) * 0.1
    elif income <= 1000000:
        tax = 37500 + (income - 750000) * 0.15
    elif income <= 1250000:
        tax = 75000 + (income - 1000000) * 0.2
    elif income <= 1500000:
        tax = 125000 + (income - 1250000) * 0.25
    else:
        tax = 187500 + (income - 1500000) * 0.3

    return round(tax)


def main():
    while True:
        try:
            ctc = int(input("Enter the CTC (in Rs): "))
            bonus = int(input("Enter the bonus (in Rs): "))
            total_income = ctc + bonus

            old_regime = old_regime_tax(total_income)
            new_regime = new_regime_tax(total_income)
            print("Total income after including bonus: Rs.", total_income)
            print("Old Regime Tax: Rs.", old_regime)
            print("New Regime Tax: Rs.", new_regime)
            #comaprision between old and new regimes and getting amount by which benifited
            if old_regime > new_regime:
                print("Benefited by New Regime by amount: Rs.", old_regime - new_regime)
            elif old_regime < new_regime:
                print("Benefited by Old Regime by amount: Rs.", new_regime - old_regime)
            else:
                print("Both regimes result are same.")

            choice = input("\nDo you want to recalculate? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("closing")
                break

        except ValueError:
            print("Please enter valid input.\n")


if __name__ == "__main__":
    main()
