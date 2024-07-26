#import math
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
print(a,b,c)
delta=((b**2)-4*a*c)
#sqrt_val=math.sqrt(delta)
if(delta>0):
    print('roots are real and different')
    print((-b + delta**0.5)/(2 * a)) 
    print((-b - delta**0.5)/(2 * a)) 
elif delta == 0: 
    print("real and same roots") 
    print(-b / (2 * a))
else:
    print("Complex Roots") 
    print(- b / (2 * a), + i,delta**0.5/ (2 * a)) 
    print(- b / (2 * a), - i,delta**0.5 / (2 * a))    