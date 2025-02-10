rollno=int(input("Enter ur rollno: "))
name=(input("Enter ur name: "))
phy=int(input("Enter ur Physics: "))
chem=int(input("Enter ur Chemistry: "))
capp=int(input("Enter ur Computer Application: "))
total=phy+chem+capp
print("Total marks: ",total)
perc=(total/300)*100
print("Percentage: ",perc)
if perc>=90:
    print("First class")
elif perc>=80:
    print("Second class")
elif perc>=70:
    print("Third class")
else:
    print("Fail")