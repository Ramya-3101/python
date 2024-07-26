unit=int(input("enter the units: "))
if unit<=50:
    amt=unit*0.50
    #print("amount is ",amt)
elif unit<=150:
    amt=25+((unit-50)*0.75)
    #print("amount is",amt)
elif unit<=250:
    amt=100+((unit-150)*1.20)
    #print("amount is",amt)
else:
    amt=220+((unit-250)*1.50)
surchrge=amt*0.20
tot_amt=amt+surchrge
print("total amount is",tot_amt)
    