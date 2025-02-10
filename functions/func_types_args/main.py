# def sum(a,b,c):
#     print(a + b + c)
    
    
# sum(3, 7)
# sum(8, 3)
# sum(4, 6)
# sum(4, 6, 7)
# sum(4, 6, 7, 9)

# def sum(*values):
#     s = 0
#     for i in values:
#         s = s + i
#     return s   
    
    
# print(sum(3, 7))
# print(sum(4, 6, 7))
# print(sum(4, 6, 7, 9))

# def person(name, age, location):
#     print("Name : ", name)
#     print("Age : ", age)
#     print("Location : ", location, "\n")
    
    
# # person('xyz', 10, "pondy.
# person(location="pondy", age=10, name='xyz')


def person(**obj):
    print(obj)
    print("Name : ", obj['name'])
    print("Age : ", obj['age'])
    print("Location : ", obj['location'], "\n")
    
    
# person('xyz', 10, "pondy.
person(location="pondy", age=10, name='xyz', gender= "male")