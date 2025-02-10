mat=int(input("enter ur maths mark: "))
phy=int(input("enter ur physics mark: "))
chem=int(input("enter ur chemistry mark: "))
total=mat+phy+chem
print("total marks: ",total)
t1=mat+phy
print("total marks of mat & phy: ",t1)
if (phy>=55 and mat>=65 and chem>=50 and total>=190) or t1>=140:
    print("candidates are eligible")
else:
    print("candidates are not eligible")