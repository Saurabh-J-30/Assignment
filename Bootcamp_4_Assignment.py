# class Car:
#     Car_color1 = "Red"
#     Car_model1 = "Nexon"
#     Car_color2 = "Green"
#     Car_model2 = "Tata"
# s1 = Car()
# print (s1)
# print (s1.Car_color1)
# print (s1.Car_model1)
# print (s1.Car_color2)
# print (s1.Car_model2)

### Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?

# class Car:
#     def __init__(self,brand, model, year):
#         self.make = brand
#         self.model = model
#         self.year = year
#     def display(self):
#         print (self.make, self.year, self.model)
# car1 = Car('Hyundai', 'Creta', 2024)
# car2 = Car('Honda', 'City', 2021)
# car3 = Car('Tata', 'Nexon', 2023)
# car1.display()
# car2.display()
# car3.display()

### 2. Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks
#     def display(self):
#         print(f"Student Details:Name: {self.name} Roll Number: {self.roll_number} Marks: {self.marks}")
# student1 = Student("Saurabh", "12345", 98)
# student2 = Student("Satish", "13578", 90)
# student3 = Student("Rahul", "54321", 88)
# student1.display()
# student2.display()
# student3.display()

### 3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         return self.length * self.breadth
#
#     def perimeter(self):
#         return 2 * (self.length + self.breadth)
#
# rectangle1 = Rectangle(10, 5)
# rectangle2 = Rectangle(7, 3)
# rectangle3 = Rectangle(12, 8)
#
# rectangles = [rectangle1, rectangle2, rectangle3]
#
# for i, rect in enumerate(rectangles, start=1):
#     print(f"Rectangle {i}:")
#     print(f"  Area: {rect.area()}")
#     print(f"  Perimeter: {rect.perimeter()}")
#     print()

### 4. Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return math.pi * (self.radius ** 2)
#
#     def get_circumference(self):
#         return 2 * math.pi * self.radius
#
# radius_input = float(input("Enter the radius of the circle: "))
# circle = Circle(radius_input)
#
# print(f"Area of circle with radius {radius_input} is: {circle.get_area():.2f}")
# print(f"Circumference of circle with radius {radius_input} is: {circle.get_circumference():.2f}")

### 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

# class Account:
#     def __init__(self, account_no, initial_balance=0):
#         self.account_no = account_no
#         self.balance = initial_balance
#
#     def credit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Credited: {amount}. New balance: {self.balance}")
#         else:
#             print("Invalid credit amount. Must be greater than zero.")
#
#     def debit(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Debited: {amount}. New balance: {self.balance}")
#         else:
#             print("Invalid debit amount. Must be greater than zero and less than or equal to the current balance.")
#
#     def print_balance(self):
#         print(f"Account No: {self.account_no}, Current Balance: {self.balance}")
#
# account = Account("12345678", 10000)  # Create an account with an initial balance
# account.credit(500)
# account.debit(150)
#
# account.print_balance()

### 6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.

# class Employee:
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         cls.employee_count += 1
#
#     @classmethod
#     def get_employee_count(cls):
#         return cls.employee_count
#
# emp1 = Employee("A")
# print(f"Current Employee Count: {Employee.get_employee_count()}")
#
# emp2 = Employee("B")
# print(f"Current Employee Count: {Employee.get_employee_count()}")
#
# emp3 = Employee("C")
# print(f"Current Employee Count: {Employee.get_employee_count()}")

### 7. Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.

# class Book:
#     def __init__(self, title, author, price=199):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def display(self):
#         print(f"Title: {self.title}, Author: {self.author}, Price: INR {self.price}")
#
# book1 = Book("The Da Vinci Code", "Dan Brown", 299)
# book2 = Book("Half Girlfriend", "Chetan Bhagat")
# book1.display()
# book2.display()

### 8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.

# class TemperatureConverter:
#     def celsius_to_fahrenheit(self, celsius):
#         return (celsius * 9/5) + 32
#
# converter = TemperatureConverter()
#
# temperatures_celsius = [0, 10, 35, 60]
# for temp in temperatures_celsius:
#     fahrenheit = converter.celsius_to_fahrenheit(temp)
#     print(f"{temp}°C is equal to {fahrenheit:.2f}°F")

### 9. Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.

# class Time:
#     def __init__(self, hours=0, minutes=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.current_time()
#
#     def current_time(self):
#
#         if self.minutes >= 60:
#             self.hours += self.minutes // 60
#             self.minutes = self.minutes % 60
#
#     def add_time(self, other):
#
#         new_hours = self.hours + other.hours
#         new_minutes = self.minutes + other.minutes
#         return Time(new_hours, new_minutes)
#
#     def __str__(self):
#         return f"{self.hours} hours and {self.minutes} minutes"
#
# time1 = Time(2, 40)
# time2 = Time(3, 55)
#
# result_time = time1.add_time(time2)
#
# print(f"Time 1: {time1}")
# print(f"Time 2: {time2}")
# print(f"Resulting Time: {result_time}")

### 10. Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.

# class EmployeeSalary:
#
#     basic_salary = 50000
#     bonus_percentage = 8
#
#     @classmethod
#     def set_bonus_percentage(cls, new_percentage):
#         cls.bonus_percentage = new_percentage
#
#     def __init__(self, name):
#         self.name = name
#
#     def calculate_total_salary(self):
#         bonus = (self.basic_salary * self.bonus_percentage) / 100
#         total_salary = self.basic_salary + bonus
#         return total_salary
#
# employee = EmployeeSalary("Sathish")
#
# print(f"{employee.name}'s Total Salary: INR {employee.calculate_total_salary():.2f}")
#
# EmployeeSalary.set_bonus_percentage(12)
#
# print(f"After changing bonus percentage:")
# print(f"{employee.name}'s Total Salary: INR {employee.calculate_total_salary():.2f}")

