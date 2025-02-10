temp=int(input("Enter the temperature in centigrade: "))
if temp<0:
    print("Freezing weather")
elif temp>=0 and temp<10:
    print("Very cold weather")
elif temp>=10 and temp<20:
    print("Cold weather")
elif temp>=20 and temp<30:
    print("Normal weather")
elif temp>=30 and temp<40:
    print("Its hot")
else:
    print("Very hot")