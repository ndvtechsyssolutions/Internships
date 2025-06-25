#MOBILE INFO 3000


# enter mobile price 
mobile_price=int(input("enter mobile price"))
#enter gst
gst_rate=int(input("enter gst rate"))
# enter discount 
discount_per=int(input("enter discount per"))
# enter additional discount per
additional_discount_per=int(input("enter additional discount per"))
#now we calculate the gst amount,discount and additional discount to get the final price of the mobile
gst_amount=(mobile_price*gst_rate)/100
price_after_gst=mobile_price+gst_amount
discount_amount=(price_after_gst*discount_per)/100
price_after_primary_discount=price_after_gst-discount_amount
additional_discount_amount=(price_after_primary_discount*additional_discount_per)/100
#here we get the final price of the mobile
final_price=price_after_primary_discount-additional_discount_amount
#now print all the statements
print("mobile_price is",mobile_price)
print("gst_amount is",gst_amount)
print("price_after_gst is",price_after_gst)
print("discount_amount is",discount_amount)
print("price_after_primary_discount is",price_after_primary_discount)
print("additional_discount_amount is",additional_discount_amount)
print("final price of the mobile is",final_price)
