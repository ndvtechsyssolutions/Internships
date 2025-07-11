def calculate_old_tax(income):
    std_deduction = 50000
    sec_80c = 150000
    taxable = income - std_deduction - sec_80c
    if taxable < 0:
        taxable = 0
    tax = 0
    if taxable <= 250000:
        tax = 0
    elif taxable <= 500000:
        tax = (taxable - 250000) * 0.05
    elif taxable <= 1000000:
        tax = 250000 * 0.05 + (taxable - 500000) * 0.2
    else:
        tax = 250000 * 0.05 + 500000 * 0.2 + (taxable - 1000000) * 0.3
    return round(tax)

def calculate_new_tax(income):
    tax = 0
    slabs = [(300000, 0), (600000, 0.05), (900000, 0.1),
             (1200000, 0.15), (1500000, 0.2), (float('inf'), 0.3)]
    prev = 0
    for limit, rate in slabs:
        if income > limit:
            tax += (limit - prev) * rate
            prev = limit
        else:
            tax += (income - prev) * rate
            break
    return round(tax)

def compare(ctc, bonus):
    total = ctc + bonus
    print("\nTotal Income:", total)
    old = calculate_old_tax(total)
    new = calculate_new_tax(total)
    print("Old Regime Tax:", old)
    print("New Regime Tax:", new)
    if old < new:
        print("Better to go with Old Regime. You save", new - old)
    elif new < old:
        print("Better to go with New Regime. You save", old - new)
    else:
        print("Both are same.")

def main():
    print("Tax Calculator - Old vs New Regime")
    while True:
        try:
            ctc = int(input("Enter your CTC: "))
            bonus = int(input("Enter your Bonus: "))
            compare(ctc, bonus)
        except:
            print("Enter valid numbers only.")
            continue
        print("\n1. Try Again\n2. Exit")
        ch = input("Choose: ")
        if ch != "1":
            break

main()
