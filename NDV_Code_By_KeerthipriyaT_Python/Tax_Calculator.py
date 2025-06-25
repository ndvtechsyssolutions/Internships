#Old regime
def old_regime(Total_Income,deduction_80c):    
  deductions=50000      #standard_deduction
  deductions += min(deduction_80c, 150000)  # Max limit of 80C is ₹1,50,000
  Total_Income -= deductions      #Total_Income=sTotal_Income-standard_deduction-80c deduction

  if Total_Income<=250000:
    return 0
  elif Total_Income<=500000:
    return (Total_Income*0.05)
  elif Total_Income<=1000000:
    return (Total_Income*0.2)
  else:
    return (Total_Income*0.3)

#New regime
def new_regime(Total_Income):
  Total_Income-=50000        #Total_Income=Total_Income-standard_deduction
  if Total_Income <= 300000:
        return 0
  elif Total_Income <= 600000:
        return (Total_Income*0.05)
  elif Total_Income <= 900000:
        return (Total_Income*0.1)
  elif Total_Income <= 1200000:
        return (Total_Income*0.15)
  elif Total_Income <= 1500000:
        return (Total_Income*0.2)
  else:
        return (Total_Income*0.3)

while True:

  Cost_To_Company=int(input("Enter your CTC:"))
  Bonus=int(input("\nEnter your Bonus:"))
  deduction_80c = int(input("Enter your 80C deductions(max ₹1,50,000): "))   #maximum RS.1,50,000

  Total_Income=Cost_To_Company+Bonus
  tax_old = old_regime(Total_Income, deduction_80c)
  tax_new = new_regime(Total_Income)

  print("Total Income:",Total_Income)
  print("\nOld Regime Tax Deduction:",tax_old)
  print("\nNew Regime Tax Deduction:",tax_new)
  if tax_old < tax_new:
    print(f"\nYou save Rs.{tax_new - tax_old} more using Old Regime")
  elif tax_new < tax_old:
    print(f"\nYou save Rs.{tax_old - tax_new} more using New Regime")
  else:
    print("\nBoth regimes result in the same tax")

  recalculate = input("\nDo you want to recalculate again? (y/n): ")
  if recalculate != 'y':
    print("Exiting Tax Calculator")
    break
