class Car:
    def __init__(self, brand, myear,color,bcapacity):
        self.brand = brand
        self.myear = myear
        self.color = color
        self.bcapacity=bcapacity
    
    def Car1(self):
        print (self.brand + " " + self.color)

# Create an instance of Student
obj1 = Car('Suzuki',2004,'Black','12W')
obj2 = Car('BMW',2007,'white','23W')
obj3 = Car('Ford',2025,'Blue','19W')

# Call the fullname method
# print(obj1.Car1())
# print(obj2.color,obj2.brand)
# print(obj3.Car1(),obj3.myear)
#print(obj2.myear)
obj1.Car1()

# class Marks:
#     def __init__(self,rollno,name,maths,physics,chemistry):
#         self.rollno=rollno
#         self.name=name
#         self.maths=maths
#         self.physics=physics
#         self.chemistry=chemistry
#     def avg(self):
#         avg=(self.maths+self.physics+self.chemistry)/3
#         return avg
# obj1=Marks(21,'Ramya',98,89,91)
# obj2=Marks(5,'Pushpaja',80,89,99)
# print(obj1.name,obj1.rollno,obj1.avg())
# print(obj2.name,obj2.avg())
