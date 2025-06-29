basic_Salary = int(input("Enter Basic Salary: "))
bonus_per = int(input("Enter Bonus Percentage: "))

bonus = basic_Salary * bonus_per / 100

deduction_per = int(input("Enter Deduction Percentage: "))
deduction = basic_Salary * deduction_per / 100

final_sal = basic_Salary + bonus - deduction

print("Basic Salary      = ", basic_Salary)
print("Bonus Amount      = ", bonus)
print("Deduction Amount  = ", deduction)
print("Final Salary      = ", final_sal)
