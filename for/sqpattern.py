n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("",end="")
    if n==1 and n%5==0:
        print(" ") 
    else:
        print("*")   
print("* "*n)


# 1st row full
# 2nd row 1st and last col 
# last full