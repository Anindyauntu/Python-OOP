

# Topic: Inheritance
# Example: Animal Kingdom
# Parent class/ Superclass: Animal
# Child class/ Subclass: Bird, Fish

class Animal:
    def  __init__(self, name, age, color): #default value deoya jay ...
        self.name = name
        self.age = age
        self.color = color
    
    def eat(self):
        print(f"{self.name} is eating. nomnomnom")
    
    def sleep(self):
        print(f"{self.name} is sleeping. zzzzzzz")




class Bird(Animal):
    def __init__(self, name, age, color, eating_habit, bird_type):
        super().__init__(name, age, color)
        self.eating_habit = eating_habit
        self.bird_type = bird_type
        
    def fly(self):
        print(f"{self.name} is flying ...")
        
    def info(self):
        print(f"I'm {self.name} & I'm a {self.bird_type} bird ...")
        
parrot =  Bird("Macaw",2,"Blue & Golden","Coconut","Parrot")
parrot.info()