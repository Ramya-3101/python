sp=int(input("Enter selling price: "))
cp=int(input("Enter cost price: "))
if sp>cp:
    profit=sp-cp
    print("profit is ",profit)
else:
    loss=cp-sp
    print("loss is ",loss)