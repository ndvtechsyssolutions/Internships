'''
#Old tax regime included following deductions and following tax slabs
#1. Standard Deductions under Section 16(ia) --> 50000
#2. Professional Tax under Section 16(iii) --> 2500(For Maharashtra)
#3. Section 80C --> 150000
#4. National Pension Scheme (if registered) under Section 80CCD(1B) --> 50000
#5. Employers Contribution to NPS (if contributes) under Section 80CCD(2) --> 10% of Basic Salary
#6. Health Insurance Premiums under Section 80D --> upto 100000
#7. Home Loan Interests Anually under Section 24(b) --> upto 200000
#8. Rent (if no House Renting Allowance) under Section 80GG --> 60000(approx)
#9. Disability & Medical under Sections 80DD/80DDB/80U --> 40000-125000
#10. Final Tax = Income Tax + 4% Cess as followes the tax slabs
            0-2.5L --> Nil
            2.5L-5L --> 5%
            5L-10L --> 20%
            >10L --> 30%
#11. If Taxable Salary is lesser than 5L after all deductions then All Taxable amounts will be Rebated under Section 87A --> upto 12500
'''
def cal_tax_old_regime(income):
    if income<=250000:
        tax=0
    elif income<=500000:
        tax=(income-250000)*0.05
    elif income<=1000000:
        tax=(250000*0.05)+(income-500000)*0.2
    elif 1000000<income:
        tax=(250000*0.05)+(500000*0.2)+(income-1000000)*0.3
    
    #Rebate in case of salary is lesser then 5L
    if income<=500000:
        tax=max(0,tax-12500)

    return tax+tax*0.04 #Including 4% Cess to the final tax amount

'''
New tax regime includes following deductions and following tax slabs
1. Standard Deductions udner Section 16(ia) --> 50000
2. Employers Contribution to NPS (if contributes) under Section 80CCD(2) --> 10% of Basic Salary
3. Final Tax = Income Tax + 4% Cess
        0-3L --> 0%
        3L-6L --> 5%
        6L-9L --> 10%
        9L-12L --> 15%
        12L-15L --> 20%
        >15L --> 30%
4. If Taxable Salary is lesser than 7L after all deductions then All Taxable amounts will be Rebated under Section 87A --> upto 25000
'''
def cal_tax_new_regime(income):
    if income<=300000:
        tax=0
    elif income<=600000:
        tax=(income-300000)*0.05
    elif income<=900000:
        tax=(300000*0.05)+(income-600000)*0.1
    elif income<=1200000:
        tax=(300000*0.05)+(300000*0.1)+(income-900000)*0.15
    elif income<=1500000:
        tax=(300000*0.05)+(300000*0.1)+(300000*0.15)+(income-1200000)*0.2
    else:
        tax=(300000*0.05)+(300000*0.1)+(300000*0.15)+(300000*0.2)+(income-1500000)*0.3
    
    #Rebate in case of salary is lesser then 7L
    if income<=700000:
        tax=max(0,tax-25000)
    
    return tax+tax*0.04

def tax_calculator():
    while True:
        print("Please mention all the mentioned details as per your offer later")

        salary= float(input("Enter your Basic Salary: "))
        bonus= float(input("Enter your Bonus in percentage: "))
        hra= float(input("Enter your Housing Rent Allowance amount (if not then press 0): "))
        sa= float(input("Enter your Special Allowance (if not then press 0): "))
        lta= float(input("Enter your Leave Travel Allowance (if not then press 0): "))
        oa= float(input("Enter your Other Allowance (if not then press 0): "))
        #Annual Salary calculated from the inputs
        annual_salary=salary+(salary*bonus/100)+hra+sa+lta+oa

        std_ded= 50000
        professional_tax= 2500
        sec_80C= 150000

        a1=int(input("Are you registered under NPS. Press 1 for yes or 0 for no: "))
        nps=50000 if a1==1 else 0

        a2=int(input("Do your Employer Contributes to NPS. Press 1 for yes or 0 for no: "))
        ecnps=salary*0.1 if a2==1 else 0

        a3=int(input("Enter your Health Insurance Premium Amount: "))
        hip=min(a3,100000)

        a4=float(input("Enter your Anual Home Loan Interest Amount(if any): "))
        hli=min(a4,200000)

        #Rent in tax deduction can be considered if we don't own any house and don't get HRA
        rent=60000 if hra==0 and hli==0 else 0

        a5= int(input("Enter Amount under Section 80DD/80DDB/80U for medical or disability treatment (if any): "))
        m_exp=min(a5,125000)

        #All the deductions counted
        deductions_old=std_ded+professional_tax+sec_80C+nps+ecnps+hip+hli+rent+m_exp
        #Now the Actual Take home Salary
        income_old_regime=annual_salary-deductions_old

        #All the deductions for new regime
        deductions_new=std_ded+ecnps
        income_new_regime=annual_salary-deductions_new

        #Tax Calculated from old regime
        tax_old=cal_tax_old_regime(income_old_regime)
        #Tax Calculated from new regime
        tax_new=cal_tax_new_regime(income_new_regime)

        print("\nComparing the Old Tax Regime with New Tax Regime")
        print(f"Annual Salary is: {annual_salary}")
        print(f"Taxable Income of the Employee in Old Regime is: {income_old_regime}")
        print(f"Taxable Income of the Employee in New Regime is: {income_new_regime}")
        print(f"Tax Amount Calculated based on the Old Regime is: {tax_old}")
        print(f"Tax Amount Calculated based on the New Regime is: {tax_new}")

        if tax_new>tax_old:
            print("Old Tax Regime is more beneficial")
        elif tax_new<tax_old:
            print("New Tax Regime is more beneficial")
        else:
            print("Both Are Same")

        print("\nDo your want to recalculate or exit")
        print("Press 1 for Recalculation or Press 0 to Exit")
        choice=int(input("Enter your choice (0 or 1): "))
        if choice!=1:
            print("Thank you for using Tax Calculator.")
            break

#Running the Calculator
tax_calculator()
