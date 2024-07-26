x=int(input("enter x: "))
y=int(input("enter y: "))
z=int(input("enter z: "))
print(x,y,z)
if(x+y>z and y+z>x and z+x>y):
    print('it is a triangle')
else:print('not a triangle')    