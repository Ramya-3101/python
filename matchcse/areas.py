print("enter 1 for area of circle:")
print("enter 2 for area of rectangle:")
print("enter 3 for area of triangle:")
area=int(input("Enter your choice: "))
match area:
    case 1:
        r=int(input("Enter radius: "))
        pi=3.14
        area=pi*r*r
        print("Area of circle= ",area)
    case 2:
        l=int(input("Enter length: "))
        w=int(input("Enter width: "))
        area=l*w
        print("Area of rectagle= ",area)
    case 3:
        b=int(input("Enter base: "))
        h=int(input("Enter height: "))
        area=(1/2)*b*h
        print("Area of triangle= ",area)
    case _:
        print("Invalid")