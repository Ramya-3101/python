#sum of natural nos
sum=0
for i in range(0,100+1):
    print(i)
    sum+=i
print("sum of natural nos: ",sum)

#sum of even nos
for i in range(2,100+1,2):
    print("Evennos: ",i)
    sum+=i
print("sum of even nos: ",sum)
#odd
for i in range(1,100,2):
    print("Oddnos: ",i)
    sum+=i
print("sum of odd nos: ",sum)