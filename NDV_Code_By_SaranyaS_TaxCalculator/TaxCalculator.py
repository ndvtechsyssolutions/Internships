def tax_calc_old(total_income):
    standard_deduction=50000
    deduction_80c=150000
    deduced_tax=total_income-standard_deduction-deduction_80c 
    tax=0
    if(deduced_tax<=250000):
        tax=0
    elif(250000<deduced_tax<=500000):
        tax=0.05
        deduced_tax=(deduced_tax-250000)*tax
    elif(500000<deduced_tax<=1000000):
        tax=0.20
        deduced_tax=(250000*0.05)+(deduced_tax-500000)*tax 
    else:  
        tax=0.30
        deduced_tax=(500000*0.20)+(250000*0.05)+(deduced_tax-1000000)*tax 

    return deduced_tax       

def tax_calc_new(total_income):
    #there is no standard deduction and 80c deduction etc 
    pay_tax_income=total_income
    tax=0
    if(pay_tax_income<=300000):
        tax=0
    elif(300000<pay_tax_income<=600000):
        tax=0.05
        pay_tax_income=(pay_tax_income-300000)*tax
    elif(600000<pay_tax_income<=900000):
        tax=0.10
        pay_tax_income=(300000*0.05)+(pay_tax_income-600000)*tax 
    elif(900000<pay_tax_income<=1200000):
        tax=0.15
        pay_tax_income=(300000*0.05)+(600000*0.10)+(pay_tax_income-900000)*tax  
    elif(1200000<pay_tax_income<=1500000):
        tax=0.20
        pay_tax_income=(300000*0.05)+(600000*0.10)+(900000*0.15)+(pay_tax_income-1200000)*tax        
    else:  
        tax=0.30
        pay_tax_income=(300000*0.05)+(600000*0.10)+(900000*0.15)+(1200000*0.20)+(pay_tax_income-1500000)*tax  

    return pay_tax_income

ctc=float(input("Enter you ctc amount:"))
bonus=float(input("Enter you bonus amount:"))
total_income=ctc+bonus
old_regime_tax=tax_calc_old(total_income)
new_regime_tax=tax_calc_new(total_income)
if(old_regime_tax<new_regime_tax) :
    print("Old regime tax saves ",new_regime_tax-old_regime_tax,"/- amount")
elif(new_regime_tax<old_regime_tax):
    print("Old regime tax saves ",old_regime_tax-new_regime_tax,"/- amount")
else:
    print("Both old regime tax and new regime tax are equal")

