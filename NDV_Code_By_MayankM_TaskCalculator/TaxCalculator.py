# --- Tax Calculator
try:
    ctc = float(input("Enter your annual CTC (₹): "))
    bonus = float(input("Enter your annual bonus (₹): "))
except ValueError:
    print(" Invalid input. Please enter numeric values.")
    ctc = 0
    bonus = 0

# --- Old Regime Tax Calculation ---
def calculate_old_regime_tax(income):
    deductions = 200000  # ₹50,000 Standard + ₹1.5L 80C (assumed)
    taxable_income = max(income - deductions, 0)

    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.20
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.30

    # 87A Rebate
    if taxable_income <= 500000:
        tax = 0

    return tax

# --- New Regime Tax Calculation ---
def calculate_new_regime_tax(income):
    slabs = [300000, 600000, 900000, 1200000, 1500000]
    rates = [0.05, 0.10, 0.15, 0.20, 0.30]

    tax = 0
    prev_slab = 0

    for i in range(len(slabs)):
        if income > slabs[i]:
            tax += (slabs[i] - prev_slab) * rates[i]
            prev_slab = slabs[i]
        else:
            tax += (income - prev_slab) * rates[i]
            return tax

    if income > 1500000:
        tax += (income - 1500000) * 0.30

    if income <= 700000:
        tax = 0

    return tax

# --- Compute Taxes ---
total_income = ctc  # Assume bonus is part of CTC
old_tax = calculate_old_regime_tax(total_income)
new_tax = calculate_new_regime_tax(total_income)

# --- Display Results ---
print("\n--- Tax Calculation Summary ---")
print(f"Total Annual Income: ₹{total_income:,.2f}")
print(f"Old Regime Tax: ₹{old_tax:,.2f}")
print(f"New Regime Tax: ₹{new_tax:,.2f}")

if old_tax < new_tax:
    print(" Better to choose: OLD Regime")
elif new_tax < old_tax:
    print(" Better to choose: NEW Regime")
else:
    print(" You save Rs.37500 more using the OLD Regime")

OUTPUT:-
Enter your annual CTC (₹): 1500000
Enter your annual bonus (₹): 200000

--- Tax Calculation Summary ---
Total Annual Income: ₹1,500,000.00
Old Regime Tax: ₹202,500.00
New Regime Tax: ₹240,000.00
 Better to choose: OLD Regime
