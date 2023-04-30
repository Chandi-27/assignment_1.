cost_of_book1=499.00
cost_of_book2=855.00
cost_of_book3=645.00

gst_rate=0.12
delivery_charges=250.00
subtotal=cost_of_book1+cost_of_book2+cost_of_book3
taxes=subtotal*gst_rate
total_invoice=subtotal+taxes+delivery_charges

print("Subtotal : Rs.",subtotal)
print("GST : Rs.",taxes)
print("Delivery_charges : Rs.",delivery_charges)
print("Total invoice : Rs.",total_invoice)