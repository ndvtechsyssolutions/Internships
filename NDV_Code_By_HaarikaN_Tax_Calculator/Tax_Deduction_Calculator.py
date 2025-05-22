def calculate_old_regime_tax(income):
    # Old regime tax slabs
    tax_slabs = [
        (0, 250000, 0),
        (250001, 500000, 0.05),
        (500001, 750000, 0.1),
        (750001, 1000000, 0.15),
        (1000001, 1250000, 0.2),
        (1250001, 1500000, 0.25),
        (1500001, float('inf'), 0.3)
    ]

    tax = 0
    for slab in tax_slabs:
        if income > slab[1]:
            tax += (slab[1] - slab[0]) * slab[2]
        else:
            tax += max(0, income - slab[0]) * slab[2]
            break

    return tax

def calculate_new_regime_tax(income):
    # New regime tax slabs
    tax_slabs = [
        (0, 250000, 0),
        (250001, 500000, 0.05),
        (500001, 750000, 0.1),
        (750001, 1000000, 0.15),
        (1000001, 1250000, 0.2),
        (1250001, 1500000, 0.25),
        (1500001, float('inf'), 0.3)
    ]

    # Standard deduction
    income -= 50000

    tax = 0
    for slab in tax_slabs:
        if income > slab[1]:
            tax += (slab[1] - slab[0]) * slab[2]
        else:
            tax += max(0, income - slab[0]) * slab[2]
            break

    return tax

def calculate_tax_deductions(ctc, bonus):
    total_income = ctc + bonus

    old_regime_tax = calculate_old_regime_tax(total_income)
    new_regime_tax = calculate_new_regime_tax(total_income)

    return total_income, old_regime_tax, new_regime_tax

def main():
    ctc = int(input("Enter your CTC: "))
    bonus = int(input("Enter your bonus: "))

    total_income, old_regime_tax, new_regime_tax = calculate_tax_deductions(ctc, bonus)

    print(f"Total income: {total_income}")
    print(f"Old regime tax deduction: {round(old_regime_tax)}")
    print(f"New regime tax deduction: {round(new_regime_tax)}")
    if old_regime_tax < new_regime_tax:
        print(f"You save {round(new_regime_tax - old_regime_tax)} more using old regime")
    elif new_regime_tax < old_regime_tax:
        print(f"You save {round(old_regime_tax - new_regime_tax)} more using new regime")
    else:
        print("Both regimes have the same tax deduction")

if __name__ == "__main__":
    main()
