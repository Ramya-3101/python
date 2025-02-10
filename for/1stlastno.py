#import math
ip=int(input("Enter a no: "))
#for i in range(1,ip+1):
#    n=ip%10
 #n1=ip//10
#print("last digit is ",n)
a=int(str(ip)[:1])
b=int(str(ip)[-1:])
print(a,b)
sum=a+b
print(sum)