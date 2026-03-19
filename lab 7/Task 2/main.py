from models import Animal, Dog, Cat

dog = Dog("Rex", 5, "brown", "shepherd")
cat = Cat("Murka", 3, "white", 9)
animal = Animal("SomeAnimal", 2, "gray")

animals = [dog, cat, animal]

for a in animals:
    print(a)
    print(a.info())
    print(a.speak())
    print()
    