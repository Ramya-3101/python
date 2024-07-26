phy=int(input("Enter ur physics mark: "))
chem=int(input("Enter ur chemistry mark: "))
bio=int(input("Enter ur biology mark: "))
mat=int(input("Enter ur maths mark: "))
com=int(input("Enter ur computer mark: "))
sum=phy+chem+bio+mat+com
print("sum:",sum)
perc=(sum/500)*100
print("percentage:",perc)
if perc>=90:
    print("grade A")
elif perc>=80:
    print("grade B")
elif perc>=70:
    print("grade C")
elif perc>=60:
    print("grade D")
elif perc>=40:
    print("grade E")
else:
    print("grade F")