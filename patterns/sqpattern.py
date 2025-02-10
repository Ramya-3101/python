n=int(input("Enter a number: "))
print("* "*n)
for i in range(1,n+1):
    print("",end="")
    if n==1 and n%5==0:
        print(" ")
    elif n==1 and n<5:
        print(" -"*5)   
    else:
        print("*")   
print("* "*n)

# 1st row full
# 2nd row 1st and last col 
# last full