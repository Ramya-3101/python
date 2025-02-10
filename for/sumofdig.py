n= input("Enter number: ")
print(n)
sum=0
pro=1
for i in n:
    sum+=int(i)
    pro*=int(i)
print("sum of digits: ",sum)
print("product of digits: ",pro)