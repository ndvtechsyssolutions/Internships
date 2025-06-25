basic_salary = int(input("enter the salary"))
bonus = int (input("enter the bonus"))
# Calculate the total before printing
total = basic_salary + bonus
print("after adding the bonus=", total)
#taking input of old regime as percentage
deduction_per_for_old_regime = float(input("enter the  old regime deduction percentage="))
old_deduction_value = total*deduction_per_for_old_regime/100
#taking input of new regime as percentage
duction_per_for_new_regime = float(input("enter the  new rigime deduction percentage="))
new_deduction_value = total*duction_per_for_new_regime/100
old_final = total-old_deduction_value
new_final = total-new_deduction_value
print("basic salary is =",basic_salary)
print("bonus is =",bonus)
print("value of old regime =",old_deduction_value)
print("value of new regime =",new_deduction_value)
print("value of old regime final value=",old_final)
print("value of new regime final value=",new_final)
OUTPUT:
enter the salary600000
enter the bonus50000
after adding the bonus= 650000
enter the  old regime deduction percentage=4
enter the  new rigime deduction percentage=5
basic salary is = 600000
bonus is = 50000
value of old regime = 26000.0
value of new regime = 32500.0
value of old regime final value= 624000.0
value of new regime final value= 617500.0
