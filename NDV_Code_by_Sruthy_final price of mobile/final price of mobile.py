# Calculating final price of mobile

mobile_price = int(input("enter mobile price:"))
GST =  int(input("enter GST:"))
discount = int(input("enter discount percentage:"))
discount_value = mobile_price*discount/100
additional_discount = int(input("enter additional_discount percentage:"))
additional_discount_value = mobile_price*additional_discount/100
total_discount = discount_value + additional_discount_value
final_price = mobile_price + GST -total_discount

print("mobile_price is:", mobile_price )
print("GST is", GST)
print("discount value is",discount_value)
print("additional discount value is", additional_discount_value)
print("total_discount is", total_discount)
print("final_price is", final_price)
