char=input("enter a character:")
if (char>='a' and char<='z') or (char>='A' and char<='Z'):
    print("it is an alphabet")
elif char>='0' and char<='9':
    print("it a digit")
else:
    print("it a spl char")