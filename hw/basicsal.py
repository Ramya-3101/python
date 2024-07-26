bsal=int(input("enter ur salary: "))
print("basic salary is ",bsal)
if bsal<=10000:
    hra=bsal*0.2
    da=bsal*0.8
    gsal=bsal+da+hra
    print("gross salary is ",gsal)
elif bsal<=20000:
    hra=bsal*0.25
    da=bsal*0.9
    gsal=bsal+da+hra
    print("gross salary is ",gsal)
else:
    hra=bsal*0.3
    da=bsal*0.95
    gsal=bsal+da+hra
    print("gross salary is ",gsal)