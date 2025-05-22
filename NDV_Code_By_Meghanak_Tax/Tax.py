
#TAX CALCULATOR


#enter ctc
ctc = float(input("Enter your CTC: "))
#enter bonus
bonus = float(input("Enter your Bonus: "))
#calculate total income
total_income = ctc + bonus
print(f"\nTotal Income: Rs.{int(total_income)}")
#we  take and sd and 80c
standard_deduction = 50000
deduction_80c = 150000
#now we analysis  the old regime and new regime
old_regime_taxable_income = total_income - standard_deduction - deduction_80c

if old_regime_taxable_income < 0:
    old_regime_taxable_income = 0

old_regime_tax = 0

if old_regime_taxable_income <= 250000:
    old_regime_tax = 0
elif 250001 <= old_regime_taxable_income <= 500000:
    old_regime_tax = (old_regime_taxable_income - 250000) * 0.05
elif 500001 <= old_regime_taxable_income <= 1000000:
    old_regime_tax = 12500 + (old_regime_taxable_income - 500000) * 0.20
else:
    old_regime_tax = 112500 + (old_regime_taxable_income - 1000000) * 0.30


new_regime_tax = 0

if total_income <= 300000:
    new_regime_tax = 0
elif 300001 <= total_income <= 600000:
    new_regime_tax = (total_income - 300000) * 0.05
elif 600001 <= total_income <= 900000:
    new_regime_tax = 15000 + (total_income - 600000) * 0.10
elif 900001 <= total_income <= 1200000:
    new_regime_tax = 45000 + (total_income - 900000) * 0.15
elif 1200001 <= total_income <= 1500000:
    new_regime_tax = 90000 + (total_income - 1200000) * 0.20
else:
    new_regime_tax = 150000 + (total_income - 1500000) * 0.30

#now print the old and new regime 
print(f"Old Regime Tax Deduction: Rs.{int(old_regime_tax):,}")
print(f"New Regime Tax Deduction: Rs.{int(new_regime_tax):,}")


if old_regime_tax < new_regime_tax:
    saving = new_regime_tax - old_regime_tax
    print(f"You Save Rs.{int(saving):,} more using the Old Regime.")
elif new_regime_tax < old_regime_tax:
    saving = old_regime_tax - new_regime_tax
    print(f"You Save Rs.{int(saving):,} more using the New Regime.")
else:
    print("Both Old and New Regimes result in the same tax deduction.")
