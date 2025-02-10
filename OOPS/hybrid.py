class Animal:
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Species: {self.species}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal): 
    def __init__(self, species, name, age, legs):
        super().__init__(species, name, age)  
        self.legs = legs
    
    def display_dog_info(self):
        print(f"Number of legs: {self.legs}")
        self.display_info()
    
    def bark(self):
        print(f"{self.name} is barking.")

class Bird(Animal):
    def __init__(self, species, name, age, wingspan):
        super().__init__(species, name, age)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} meters.")

class Puppy(Dog):
    def __init__(self, name, age, legs, breed):
        super().__init__('Dog-Puppy', name, age, legs)
        self.breed = breed
    
    def display_puppy_info(self):
        print(f"Breed: {self.breed}")
        self.display_dog_info()

animal = Animal("Generic Animal", "Charlie", 5)
dog = Dog("Dog", "Max", 3, 4)
bird = Bird("Parrot", "Coco", 2, 0.5)
puppy = Puppy("Buddy", 1, 4, "Golden Retriever")

print("Animal Info:")
animal.display_info()
animal.eat()
animal.sleep()

print("\nDog Info:")
dog.display_dog_info()
dog.bark()

print("\nBird Info:")
bird.display_info()
bird.fly()

print("\nPuppy Info:")
puppy.display_puppy_info()
puppy.bark()
