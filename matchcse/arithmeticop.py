print("enter 1 for Addition:")
print("enter 2 for Subraction:")
print("enter 3 for Multiplication:")
print("enter 4 for Division:")
option=int(input("Enter your option: "))
match option:
    case 1:
        n1=int(input("Enter 1st no: "))
        n2=int(input("Enter 2nd no: "))
        add=n1+n2
        print("Additon of two nos = ",add)
    case 2:
        n1=int(input("Enter 1st no: "))
        n2=int(input("Enter 2nd no: "))
        sub=n1-n2
        print("Subraction of two nos = ",sub)
    case 3:
        n1=int(input("Enter 1st no: "))
        n2=int(input("Enter 2nd no: "))
        mul=n1*n2
        print("Multiplication of two nos = ",mul)
    case 4:
        n1=int(input("Enter 1st no: "))
        n2=int(input("Enter 2nd no: "))
        if n2==0:
            print("Division not possible")
        else:
            div=n1/n2
            print("Divison of two nos = ",div)
    case _:
        print("Invalid")