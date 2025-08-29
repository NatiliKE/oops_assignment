"""
Assignment 1 & Activity 2: Object-Oriented Programming in Python
Author: Your Name
Date: YYYY-MM-DD
"""

# ----------------------------------------------------------
# Assignment 1: Design Your Own Class (Smartphone Example) 🏗️
# ----------------------------------------------------------

# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Derived Class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Call parent constructor
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.brand} {self.model}...")

    def charge(self):
        print(f"🔋 Charging {self.brand} {self.model}... Battery at {self.battery}%")

    # Polymorphism (overriding parent method)
    def info(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%"


# Create Smartphone objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 85)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 60)

print("----- Smartphone Info -----")
print(phone1.info())
phone1.make_call("+123456789")
phone1.charge()

print(phone2.info())
print()

# ----------------------------------------------------------
# Activity 2: Polymorphism Challenge 🎭
# ----------------------------------------------------------

class Vehicle:
    def move(self):
        print("The vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky!")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water!")


print("----- Vehicle Movements -----")
vehicles = [Car(), Plane(), Boat()]  # List of different vehicles

for v in vehicles:
    v.move()
