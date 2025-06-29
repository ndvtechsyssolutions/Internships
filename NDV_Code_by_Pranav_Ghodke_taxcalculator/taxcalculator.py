total_ctc=float(input("Enter the Total CTC:")) #input from user
total_bonusamt=float(input("Enter the Total Bonus Amount:")) #input from user
standard_ded=50000
section_80C=150000
total_income=total_ctc+total_bonusamt
print("Total Income:",total_income) #total income after including ctc and bonus amount

taxable_income=total_income-(standard_ded+section_80C) #taxable income after the deduction

print("Taxable income:",taxable_income)
#By using conditional statements(Nested if-elif-else)
if taxable_income <=250000:
    old=0
    new=0
    print("Old regime:",old)
    print("New Regime:",new)
    #compare new regime and old regime tax deduction to know which tax regime saves money
    if new<old:
        print("You save RS ",old-new," Using new regime")
    elif new>old:
        print("You save RS ",new-old," Using old regime")
    else:
        print("You have not saved anything")

elif taxable_income <=500000:
    old=taxable_income*5/100
    new=taxable_income*5/100
    print("Old regime:",old)
    print("New Regime:",new)
    if new<old:
        print("You save RS ",old-new," Using new regime")
    elif new>old:
        print("You save RS ",new-old," Using old regime")
    else:
        print("You have not saved anything")

elif taxable_income <=1000000:
    old=taxable_income*20/100
    new=taxable_income*10/100
    print("Old regime:",old)
    print("New Regime:",new)
    if new<old:
        print("You save RS ",old-new," Using new regime")
    elif new>old:
        print("You save RS ",new-old," Using old regime")
    else:
        print("You have not saved anything")

else:
    old=taxable_income*20/100
    new=taxable_income*15/100
    print("Old regime:",old)
    print("New Regime:",new)
    if new<old:
        print("You save RS ",old-new," Using new regime")
    elif new>old:
        print("You save RS ",new-old," Using old regime")
    else:
        print("You have not saved anything")
