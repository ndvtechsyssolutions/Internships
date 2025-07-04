sal = int(input("Enter salary: "))
bon = int(input("Enter bonus: "))
tot = sal + bon
print("Total with bonus =", tot)

old_pct = float(input("Old regime deduction %: "))
old_val = tot * old_pct / 100

new_pct = float(input("New regime deduction %: "))
new_val = tot * new_pct / 100

old_final = tot - old_val
new_final = tot - new_val

print("Salary =", sal)
print("Bonus =", bon)
print("Old regime deduction =", old_val)
print("New regime deduction =", new_val)
print("Old regime final =", old_final)
print("New regime final =", new_final)



#output

# Enter salary: 50000
# Enter bonus: 10000
# Total with bonus = 60000
# Old regime deduction %: 10
# New regime deduction %: 5
# Salary = 50000
# Bonus = 10000
# Old regime deduction = 6000.0
# New regime deduction = 3000.0
# Old regime final = 54000.0
# New regime final = 57000.0
