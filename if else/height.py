h=int(input("enter your height in cm: "))
if h<150 and h>50:
    print("dwarf")
elif h==150:
    print("average")
elif h>150:
    print("tall")
else:
    print("incorrect")