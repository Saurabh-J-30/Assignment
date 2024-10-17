### Assignment 1: Static Methods
### Create a class MathOperations that contains:
### A static method add_numbers that takes two arguments and returns their sum.
### A static method multiply_numbers that takes two arguments and returns their product.


# class MathOperations:
#     @staticmethod
#     def add_numbers(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply_numbers(a, b):
#         return a * b
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# sum_result = MathOperations.add_numbers(num1, num2)
# product_result = MathOperations.multiply_numbers(num1, num2)
#
# print(f"The sum of {num1} and {num2} is: {sum_result}")
# print(f"The product of {num1} and {num2} is: {product_result}")

### Assignment 2: Class Methods
### Create a class Person that keeps track of the number of people created. The class should have:
### A class variable count to count instances of the class.
### A class method get_count that returns the current count.

# class Person:
#     count = 0
#
#     def __init__(self):
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# person1 = Person()
# person2 = Person()
# person3 = Person()
#
# print(f"Number of people created: {Person.get_count()}")

### Assignment 3: Using Both Static and Class Methods
### Create a class TemperatureConverter with the following:
### A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
### A class method info that returns a message about temperature conversions.

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
#     @classmethod
#     def info(cls):
#         return "This method convert temperatures from Celsius to Fahrenheit."
#
#
# celsius_temp = float(input("Enter temperature in Celsius: "))
# fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
# print(f"{celsius_temp}°C is equivalent to {fahrenheit_temp:.2f}°F")
# print(TemperatureConverter.info())

### Assignment 4: Single Inheritance
### Create two classes:
### Animal with a method sound that prints "Animal sound".
### Dog that inherits from Animal and overrides the sound method to print "Bark".

# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# animal = Animal()
# animal.sound()
#
# dog = Dog()
# dog.sound()

### Assignment 5: Multiple Inheritance
### Create two classes:
### Bird with a method fly that prints "Flying".
### Fish with a method swim that prints "Swimming".
### A class Duck that inherits from both Bird and Fish.

# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     pass
#
# duck = Duck()
#
# duck.fly()
# duck.swim()

### Assignment 6: Abstract Class
### Use the abc module to create an abstract class Shape that contains:
### An abstract method area().
### Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method.

# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# circle = Circle(5)
# rectangle = Rectangle(10, 15)
#
# print(f"Area of the circle: {circle.area():.2f}")
# print(f"Area of the rectangle: {rectangle.area():.2f}")

### Assignment 7: Encapsulation
### Create a class BankAccount that uses encapsulation:
### Private attributes _balance.
### Public methods deposit() and withdraw() that modify _balance safely.

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#
#         self._balance += amount
#         print(f"Deposited: INR {amount:.2f}. New balance: INR {self._balance:.2f}")
#
#     def withdraw(self, amount):
#
#         self._balance -= amount
#         print(f"Withdrew: INR {amount:.2f}. New balance: INR {self._balance:.2f}")
#
#     def get_balance(self):
#
#         return self._balance
#
# account = BankAccount(1000)
#
# account.deposit(300)
# account.withdraw(500)
# account.withdraw(300)
#
# print(f"Current balance: INR {account.get_balance():.2f}")


### Assignment 8: Polymorphism with Method Overriding
### Create two classes Cat and Dog with a method speak().
### The Dog class should implement speak() to print "Woof".
### The Cat class should implement speak() to print "Meow".

# class Cat:
#     def speak(self):
#         print("Meow")
#
# class Dog:
#     def speak(self):
#         print("Woof")
#
# # Example usage:
# def animal_sound(animal):
#     animal.speak()
#
# dog = Dog()
# cat = Cat()
#
# animal_sound(dog)
# animal_sound(cat)

### Assignment 9: Polymorphism with Method Overloading
### Create a class Calculator with a method add() that:
### Can accept 2 or 3 arguments and returns their sum.
### Hint: Use default parameters to handle method overloading in Python.

# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
#
# calc = Calculator()
#
# sum_two = calc.add(5, 10)
# print(f"Sum of 5 and 10 is: {sum_two}")
#
# sum_three = calc.add(5, 10, 15)
# print(f"Sum of 5, 10, and 15 is: {sum_three}")

### Assignment 10: Multilevel Inheritance
### Create three classes:
### LivingBeing with a method breathe() that prints "Breathing".
### Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
### Human that inherits from Mammal and adds a method think() that prints "Thinking".

# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
#
# human = Human()
#
# human.breathe()
# human.walk()
# human.think()
