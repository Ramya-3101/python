class Animal:
    def __init__(self,species,name,age):
        self.species=species
        self.name=name
        self.age=age
    def display_info(self):
        print(f"Species = {self.species}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
    def eat(self):
        print(" animals will eat")
    def sleep(self):
        print("animals will sleep")
class Dog(Animal): 
    def __init__(self,species, name, age, legs):
        super().__init__(species, name, age)  
        self.legs=legs
    def display_Dog_info(self):
        print(f'Breed = {self.breed}')
    def bark(self):
        print('Dog barks')
class Puppy(Dog):
    def __init__(self,name, age, legs,breed):
        super().__init__('Dog-puppy', name, age, legs)
        self.breed=breed
    def display_puppy_info(self):
        print(f'Breed = {self.breed}')
        self.display_Dog_info()
        self.display_info()
obj1=Puppy('Diana',8,4,'Retriver')
obj1.display_info()
obj1.bark()
print(obj1.breed)