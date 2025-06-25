#console-base tax calculator using python
ctc = int(input("enter your ctc:"))
bonus = int(input("enter your bonus:"))
result = ctc+bonus
print("total income:RS.",result)


old = int(input("old Regime tax Dedution:RS."))
new = int(input("new Regime tax Dedution:RS."))

save = new-old

print(f"you save Rs.{save} more using the old Regime")
