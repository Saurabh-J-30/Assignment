#### Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
### Addition
### Subtraction
### Multiplication
### Division
### Modulus
### Display the results for each operation.
from xml.sax.handler import property_interning_dict

# A = float(input("Enter fist number: "))
# B = float(input("Enter second number: "))

# print ("Sum: ", A+B)
# print ("Subtraction: ", A-B)
# print ("Multiplication: ", A * B)
# print ("Division: ", A/B)
# print ("Modulus: ", A%B)

### Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.

# A = float (input("Enter the number to check if it is even or odd: "))
# B = 0
# if A % 2 == 0 :
#     print ("A is even")
# else: print ("A is odd")

### Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.

# A = float (input("Enter the number to check if it is positive, negative, or zero: "))
# if A > 0:
#     print (" A is positive number")
# elif A==0:
#     print ("A is zero")
# else: print ("A is negative number")

### Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
### 90 and above: A
### 80 - 89: B
### 70 - 79: C
### 60 - 69: D
### Below 60: F

# Marks = float (input(" Enter the marks obtained by student: "))
# if Marks >= 90:
#    print (" Student Grade is A")
# elif Marks >= 80 and Marks < 89:
#    print (" Student Grade is B")
# elif Marks >= 70 and Marks < 79:
#    print ("Student grade is C")
# elif Marks >= 60 and Marks < 69:
#    print ("Student Grade is D")
# else:  print ("Student Grade is F")

### Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.

# file = open("sample.txt","w")
# file.write("Hello, this is a sample file.")
# file.close()
# file = open("sample.txt", "r")
# content = file.read()
# print (content)
# file.close()

### Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.

# file = open("data.txt", "w")
# file.write("Hello \n")
# lines = ("This is Bangalore \n", "This is Jaipur \n", "This is London \n")
# file.writelines (lines)
# file.close()
# file = open("data.txt", "r")
# content = file.read()
# print (content)
# lines = content.split()
# number_of_words= len(lines)
# print ("Total number of words in file is:", number_of_words)
# file.close()


### Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.

# for i in range(1, 11):
#     print(i)

### Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.

# Number = int(input("Enter the number for multiplication table:"))
# for i in range(1,11):
#     print (Number, 'X', i, '=', Number*i)
