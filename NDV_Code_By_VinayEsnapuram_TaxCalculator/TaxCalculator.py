#TAX DEDUCTIONS
income=float(input(print("ENTER YOUR ANNUAL CTC ")))
bonus=float(input(print("ENTER YOUR ANNUAL BONUS ")))

net=income+bonus
print("TOTAL INCOME ..=Rs.",net)
print()

#HRA CALCULATION
if net<300000:                         #LOW SALARY
  hra=0
elif net > 300000 and net < 1000000:   #MEDIUM SALARY
  hra=0.06
elif net ==1000000 and net>1000000:   #HIGH SALARY
  hra=0.09

#STANDARD DEDUCTION
sd=50000

#80C
if net<300000:
  c=0.06
elif net > 300000 and net < 1000000:
  c=0.04
elif net ==1000000 and net>1000000:
  c=0.02


#OLD REGIEME DEDUCTION
old_regime_deduction=net * hra + sd + net * c
print("OLD REGIEME TAX DEDUCTION Rs.",old_regime_deduction)
print()

#CESS
cess=0.04

#slabs
if net<300000:
  n=0.02
elif net > 300000 and net < 1000000:
  n=0.05
elif net ==1000000 and net>1000000:
  n=0.08

#NEW REGIME DEDUCTION
new_regime_deduction=net * cess + net * n+sd
print("NEW REGIEME TAX DEDUCTION Rs.",new_regime_deduction)
print()

#SUMMARY
if new_regime_deduction < old_regime_deduction:
  print("YOU SAVE Rs. ",old_regime_deduction-new_regime_deduction,"more on NEW REGIME DEDUCTION")
elif new_regime_deduction > old_regime_deduction:
  print("YOU SAVE Rs. ",new_regime_deduction-old_regime_deduction,"more on OLD REGIME DEDUCTION")
