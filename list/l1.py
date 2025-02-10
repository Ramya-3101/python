numbers=[4,17,6,7,9,10,50,55]
even=[]
odd=[]
for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(even)
print(odd)