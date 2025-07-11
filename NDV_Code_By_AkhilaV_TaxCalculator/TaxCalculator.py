#Taking the ctc and bonus from the user 

ctc=int(input('Enter Your CTC'))
Bonus=int(input("Enter Your Bonus"))

#Assigning values to variables for tax calcualtion
standard_deduction=50000
deduction_80C=150000
deduction_80D=25000
tax_old=0
tax_new=0
amount_old=0
amount_new=0


# Tax Payable income according old Regime --subtracting the deductions like standard deduction,80C and 80D
#Assuming these are applicable

if(ctc>250000):
    amount_old=ctc+Bonus-standard_deduction-deduction_80C-deduction_80D
    
# Tax Payable income according new Regime --subtracting only standard deduction 
if(ctc>300000):
    amount_new=ctc+Bonus-standard_deduction

#According to old regime tax values are (upto 2.5L) -nil,(2.5L-5L)-5% ,(5l-10L)-20%, (>10L)-30%
if(amount_old>1000000):
    tax_old=12500+100000+(amount_old-1000000)*0.30
elif(amount_old>500000 and amount_old<=1000000):
    tax_old=12500+(amount_old-500000)*0.20
elif(amount_old>250000 and amount_old<=500000):
    tax_old=(amount_old-250000)*0.05
else:
    tax_old=0


#According to new regime tax values are (upto 3L) -nil,(3L-6L)-5% ,(6L-9L)-10%, (9L-12L)-15%
#(12L-15L)-20%, (> 15L)-30%

if(amount_new>1500000):
    tax_new=15000+30000+45000+60000+(amount_new-1500000)*0.30
elif(amount_new>1200000 and amount_new<=1500000):
    tax_new=15000+30000+45000+(amount_new-1200000)*0.20
elif(amount_new>900000 and amount_new<=1200000):
    tax_new=15000+30000+(amount_new-900000)*0.15
elif(amount_new>600000 and amount_new<=900000):
    tax_new=15000+(amount_new-600000)*0.10
elif(amount_new>300000 and amount_new<=600000):
    tax_new=(amount_new-300000)*0.05
else:
    tax_new=0

#Outputs
 
print("Total Income:",ctc+Bonus)
print("Old Regime Tax Payable Income:",amount_old)
print("New Regime Tax Payable Income:",amount_new)
print("Old Regime Total deductions:",ctc+Bonus-amount_old)
print("New Regime Total deductions:",ctc+Bonus-amount_new)
print("Old Regime Total Tax:",tax_old)
print("New Regime Total Tax:",tax_new)

if(tax_old==tax_new):
    print("Both are equal")
elif(tax_old>tax_new):
    print("You Save",tax_old-tax_new,"more using the new regime")
else:
    print("You Save",tax_new-tax_old,"more using the old regime")
