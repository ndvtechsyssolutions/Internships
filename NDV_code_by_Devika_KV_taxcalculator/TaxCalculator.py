ctc = int(input("Enter your CTC : "))
bonus = int(input("Enter your Bonus : "))

income = ctc + bonus

#old tax regime
taxable_old = income - 50000 - 150000

if taxable_old <= 250000:
    old_tax = 0
elif taxable_old <= 500000:
    old_tax = (taxable_old - 250000) * 0.05
elif taxable_old <= 1000000:
    old_tax = 12500 + (taxable_old - 500000) * 0.2
else:
    old_tax = 112500 + (taxable_old - 1000000) * 0.3

#new tax regime
if income <= 300000:
    new_tax = 0
elif income <= 600000:
    new_tax = (income - 300000) * 0.05
elif income <= 900000:
    new_tax = 15000 + (income - 600000) * 0.1
elif income <= 1200000:
    new_tax = 45000 + (income - 900000) * 0.15
elif income <= 1500000:
    new_tax = 90000 + (income - 1200000) * 0.2
else:
    new_tax = 150000 + (income - 1500000) * 0.3


print("Total Income:", income)
print("Old Regime Tax: ₹", old_tax)
print("New Regime Tax: ₹", new_tax)

diff=abs(old_tax-new_tax)
if old_tax < new_tax:
    print("You save Rs.",diff," using the Old Regime.")
elif new_tax < old_tax:
    print("You save Rs.",diff," using6 the New Regime.")
else:
    print("Both regimes give the same tax.")

print("Thank you!") 
