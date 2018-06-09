quant=int(input("Enter the quantity purchased"))
cost=quant*100
print("Total cost is", cost)
discount=(10*cost)/100
if(cost>1000):
    print("Discount offered!")
    cost=cost-discount
    print("Cost for the user after discount is", cost)
else:
 print("No discount offered")
 print("Cost remains", cost)
