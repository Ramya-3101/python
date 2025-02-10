ip=int(input("Enter a number: "))
a=int(str(ip)[:1])
b=int(str(ip)[-1:])
d=int(str(ip)[:2])
print(a,d,b)
c=a
a=b
b=c
print(a,d,b)