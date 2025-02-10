ip=int(input("Enter a number: "))
sum=0
pro=1
for i in range(1,ip+1):
    no=int(input("Enter a value: "))
    sum=sum+no
    pro=pro*no
print ("Sum=",sum)
print("Product=",pro)