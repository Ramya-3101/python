row=int(input("Enter number: "))
col=int(input("Enter number: "))
c=1
loops=row*col+1
for i in range(1,loops):
    print(c,end=" ")
    c+=1
    if i % col ==0:
        print() 
        c=1 

#reverse
# c=5
# loops=row*col
# for i in range(loops,0,-1):
#     print(c,end=" ")
#     c-=1
#     if c==0:
#         print() 
#         c=5
    

# for i in range(1,loops):
#     print("{:3d}".format(i),end=" ")
#     if i % 5==0:
#         print()

# for i in range(loops,0,-1):
#     print("{:3d}".format(i),end=" ")
#     if i==0:
#         print() 