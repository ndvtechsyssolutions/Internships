def old_regime(bs,b,d):
    tax_deduction=bs*0.1
    final_salary=bs+b-tax_deduction
    return final_salary
def new_regime(bs,b,d):
    tax_deduction=bs*0.07
    final_salary=bs+b-tax_deduction
    return final_salary
basic_salary=float(input("Enter basic salary:"))
bonus=float(input("Enter bonus:"))
deduction=float(input("Enter deduction:"))
old__regime=old_regime(basic_salary,bonus,deduction)
new__regime=new_regime(basic_salary,bonus,deduction)
print(f"Old regime salary:{old__regime}")
print(f"New regime salary:{new__regime}")
