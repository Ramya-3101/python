x=int(input("enter x: "))
y=int(input("enter y: "))
z=int(input("enter z: "))
print(x,y,z)
if(x==y==z):
    print('equalateral')
elif(x==y or x==z or y==z):
    print('isoceles')
else:print('scalene')