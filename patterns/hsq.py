n=int(input('Enter value: '))
# row=1
# col=1
# for i in range (1,7): 
#    print("* ",end="")
#    if row==1 or row==6:   
#       print("* ",end="")
#    else:
#       print(" ",end="")   

for i in range(1,n+1):
   #print("* ",end="")
   if i==1 or i==5:
      print("*",end=" ")
   else:
      print(" "*5)   