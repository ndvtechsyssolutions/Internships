annual_ctc = int(input("Enter your annual CTC: "))
yearly_bonus = int(input("Enter yearly bonus: "))
house_rent_allowance = int(input("Enter HRA: "))
basic_deduction = 50000
section_80c_deduction = 150000
total_income = annual_ctc + yearly_bonus
old_regime_taxable = total_income - basic_deduction - section_80c_deduction
new_regime_taxable = total_income - basic_deduction
print("Taxable income under Old Regime:", old_regime_taxable)
print("Taxable income under New Regime:", new_regime_taxable)
