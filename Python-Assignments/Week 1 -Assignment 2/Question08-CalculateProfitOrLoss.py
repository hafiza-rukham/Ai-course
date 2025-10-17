cost_price=int(input("Enter cost price:"))
selling_price=int(input("Enter selling price:"))
profit=selling_price-cost_price
loss=cost_price-selling_price
print("calculate profit",profit)
print("calculate loss",loss)
print("not equal",profit!=loss)