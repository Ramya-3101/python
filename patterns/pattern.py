# ip=int(input("Enter a no: "))
# for i in range(1,ip+1):
#     #print("*", end='*')
#     if ip%i==0:
#         print("\n")
#         print("*",end='*')

# for i in range(10):
#     print(i)
matrix = int(input("Enter number : ")) + 1

for i in range(1, matrix):
    print("{:2d} ".format(i) * matrix)

for i in range(1, matrix):
    print("* " * matrix)

# loops = (matrix**2)

# for i in range(1, loops):
#     print("{:3d}".format(i), end="")
#     if i % matrix == 0:
#         print()

# for i in range(1, matrix):
#     print("✨ " * i)

# for i in range(matrix, 0, -1):
#     print("✨ " * i)

# space = matrix

# for i in range(1, matrix):
#     print(" " * space, end="")
#     print("# " * i)
#     space -= 1


    #     *
    #    * *
    #   * * *
    #  * * * *
    # * * * * *

# for i in range(space,0,-1):
#     print(" ", end="")
#     print("* ",end="")
#     space+=1