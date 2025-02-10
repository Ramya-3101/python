# a=5
# b=3
# c=8
# d=3
# e=0
# f=0
# g=0
# def sum(a,b):
#     global e,f,g
#     e=a+b
#     f=c-d
#     g=e*f
# sum(a,b)     
# print(e) 
# print(f) 
# print(g) 
   
a=8
b=3
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
sum(a,b)
sub(a,b)
mul=sum(a,b)*sub(a,b)
print(mul)