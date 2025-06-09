def old_regime(tot_inc):
    standard_deduction = 50000
    sec_80C = 150000
    taxable_income = max(0, tot_inc - standard_deduction - sec_80C)
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.20
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.30
    return round(tax + (tax * 0.04))

def new_regime(tot_inc):
    tax = 0
    if tot_inc <= 300000:
        tax = 0
    elif tot_inc <= 700000:
        tax = (tot_inc - 300000) * 0.05
    elif tot_inc <= 1000000:
        tax = 20000 + (tot_inc - 700000) * 0.10
    elif tot_inc <= 1200000:
        tax = 50000 + (tot_inc - 1000000) * 0.15
    elif tot_inc <= 1500000:
        tax = 80000 + (tot_inc - 1200000) * 0.20
    else:
        tax = 140000 + (tot_inc - 1500000) * 0.30
    return round(tax + (tax * 0.04))

tot_ctc = int(input("Enter total CTC.."))
tot_bonus = int(input("Enter Bonus Amount.."))
tot_inc = tot_ctc + tot_bonus
if tot_ctc < 0 or tot_bonus < 0:
    print("\n Error: CTC and Bonus cannot be negative. \n")
else:
    old_regime = old_regime(tot_inc)
    new_regime = new_regime(tot_inc)
    print("\nTotal Income: Rs.",tot_inc)
    print("\n Old Regime Tax Deduction: Rs.",old_regime)
    print("\n New Regime Tax Deduction: Rs.",new_regime)
    if old_regime < new_regime:
        print(f"You Save Rs.{new_regime - old_regime} more using the Old Regime. \n")
    elif new_regime < old_regime:
        print(f"You Save Rs.{old_regime - new_regime} more using the New Regime. \n")
    else:
        print("\n Both regimes result in the same tax amount. \n")
