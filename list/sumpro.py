list=[2,32,4,5,11,7]
l=len(list)
sum=0
pro=1
for i in range(l):
    sum+=list[i]
    pro*=list[i]
print("sum: ",sum)
print("product: ",pro)