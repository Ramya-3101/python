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
    def __init__(self, name, age, breed, has_tails='true'):
        super().__init__('Dog', name, age)  
        self.breed=breed
        self.has_tails=has_tails
    def display_Dog_info(self):
        print(f'Breed = {self.breed}')
        print(f'Tails = {self.has_tails}')
        self.display_info()
    def bark(self):
        print('Dog barks')
class Cat(Animal):
    def __init__(self, name, age,weight):
        super().__init__('Cat', name, age)
        self.weight=weight
    def display_Cat_info(self):
        print(f'Weight = {self.weight}')
        self.display_info()
    def meow(self):
        print('Cat meows')
obj1=Cat('Nyke', '3mon', '5kg')
obj2=Dog('Ziya','8mon','Beagle')
obj1.display_Cat_info()
obj1.meow()
obj2.display_Dog_info()
obj2.bark()
print(obj1.name)
print(obj2.name)
        