current_salary = int(input("Enter your CTC "))
bonus = int(input("Enter your bonus :"))
total_salary = bonus + current_salary
old_regime = 0
new_regime = 0
if(total_salary > 0 and total_salary <= 1200000 ):
    old_regime =  total_salary - (total_salary)*0.06
    new_regime = total_salary
    print("Old regime tax deduction is :",old_regime)
    print("New regime tax deduction is :",new_regime)
    
elif(total_salary > 1200000  and total_salary <= 2000000 ):
    old_regime = total_salary - (total_salary)*0.12
    new_regime = total_salary - (total_salary)*0.10
    print("Old regime tax deduction is :",old_regime)
    print("New regime tax deduction is :",new_regime)
elif(total_salary > 2000000 and total_salary < 10000000 ):
    old_regime = total_salary - (total_salary)*0.35
    new_regime = total_salary - (total_salary)*0.20
    print("Old regime tax deduction is :",old_regime)
    print("New regime tax deduction is :",new_regime)
else:
    print("invalid")
if(old_regime > new_regime):
    print("you save ",old_regime-new_regime,"by  old regime \n")
if(old_regime < new_regime):
    print("you save ",new_regime-old_regime,"by new regime \n")
