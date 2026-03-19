class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self) -> str:
        return "Some sound"
    
    def info(self):
        return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.name} ({self.color})"
    

class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
    
    def speak(self) -> str:
        return "Woof!"
    
    def guard(self):
        return f"{self.name} is guarding"
    
class Cat(Animal):
    def __init__(self, name, age, color, lives):
        super().__init__(name, age, color)
        self.lives = lives

    def speak(self) -> str:
        return "Meow!"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    
    