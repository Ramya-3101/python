class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Species = {self.species}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")

    def eat(self):
        print("Animals eat.")

    def sleep(self):
        print("Animals sleep.")


class Dog(Animal): 
    def __init__(self, name, age, breed, has_tails=True):
        super().__init__('Dog', name, age)  
        self.breed = breed
        self.has_tails = has_tails

    def display_Dog_info(self):
        print(f"Breed = {self.breed}")
        print(f"Has tails = {self.has_tails}")
        self.display_info()

    def bark(self):
        print("Dog barks.")


class Cat(Animal):
    def __init__(self, name, age, weight):
        super().__init__('Cat', name, age)
        self.weight = weight

    def display_Cat_info(self):
        print(f"Weight = {self.weight}")
        self.display_info()

    def meow(self):
        print("Cat meows.")
print("Animal Info:")
animal = Animal("Generic Animal", "Charlie", 5)
animal.display_info()
animal.eat()
animal.sleep()

print("\nDog Info:")
dog = Dog("Buddy", 3, "Golden Retriever", True)
dog.display_Dog_info()
dog.bark()
dog.eat()
dog.sleep()

print("\nCat Info:")
cat = Cat("Luna", 2, 4.5)
cat.display_Cat_info()
cat.meow()
cat.eat()
cat.sleep()

