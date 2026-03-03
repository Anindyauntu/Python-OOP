# Polymorphism --- name will remain same but behaviour will be different ...

class Animal():
    def __init__(self):
        print("Animal Created.")
        
    def speak(self):
        print("Animal made a sound.")
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog is created.")
        
    def speak(self):
        print("The dog barked..")
    
class Cat(Animal):
    def __init__(self):
        super().__init__()
        
    def speak(self):
        print("The cat meowed.")
        
bob = Dog()
simba = Cat()

animals = [Dog(),Cat()]

animals[0].speak()
animals[1].speak()

for item in animals:
    item.speak()

