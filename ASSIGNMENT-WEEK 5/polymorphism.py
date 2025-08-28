# Polymorphism Challenge 🎭

class Animal:
    def move(self):
        pass  # to be overridden by subclasses

class Dog(Animal):
    def move(self):
        print("Running 🐕")

class Bird(Animal):
    def move(self):
        print("Flying 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming 🐟")

class Vehicle:
    def move(self):
        pass  # to be overridden by subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Polymorphism in action!
things = [Dog(), Bird(), Fish(), Car(), Plane(), Boat()]

for thing in things:
    thing.move()
