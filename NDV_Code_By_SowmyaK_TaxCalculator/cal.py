ctc=int(input("Enter ctc:"))
bonus=int(input("Enter bonus:"))
hra=int(input("Enter hra:"))
standard_deduction=50000
deduction80C=150000
gross_income=ctc+bonus
taxable_old_regime=gross_income-standard_deduction-deduction80C
taxable_new_regime=gross_income-standard_deduction
print("tax Income of old regime:", taxable_old_regime)
print("tax Income of new regime:", taxable_new_regime)
