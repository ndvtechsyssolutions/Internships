#mobile price calculator(mini project)
mobile_price=int(input("Enter price of mobile"))
gst_perc=int(input("Enter GST percentage"))
gst_val=mobile_price*gst_perc/100
discount_perc=int(input("Enter discount percentage"))
discount_val=mobile_price*discount_perc/100
additional_discount_perc=int(input("Enter  additional discount percentage"))
additional_discount_val=mobile_price*additional_discount_perc/100
final_price=mobile_price+gst_val-discount_val-additional_discount_val
print("final price of mobile is...",final_price)
