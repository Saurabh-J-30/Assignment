### Write a Python function to find the maximum of three numbers.
# numbers = [7, 18, 20]
# print (f"Max: {max(numbers)}")

### Write a Python function to multiply all the numbers in a list.
# def multiply(a,b,c,d,e):
#     return a*b*c*d*e
# result = multiply(8,2,3,-1,7)
# print (result)

### Write a Python program to reverse a string. (need to check)
# def reverse(s):
#     string = ""
#     for i in s:
#         string = i + string
#     return string
# s = "1234abcd"
# print("The original string is : ", s)
# print("The reversed string is : ", reverse(s))


# def reverse(s):
#     string = "".join(reversed(s))
#     return string
# s = "1234abcd"
#
# print("The original string is : ", s)
# print("The reversed string is : ", reverse(s))


### Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)
# n = int(input("Input a number to compute the factorial: "))
# print(factorial(n))


### Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def unique_list(list):
#     x = []
#     for a in list:
#         if a not in x:
#             x.append(a)
#     return x
#
# list= [1,2,3,3,3,3,4,5]
# print(unique_list(list))

### Write a Python function that takes a number as a parameter and checks whether the number is prime or not.





### Write a Python program to print the even numbers from a given list.
# Number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = list(filter(lambda x: (x % 2 == 0), Number))
# print (even)


### Write a Python function that accepts a string and counts the number of upper and lower case letters.
# String="The quick Brow Fox"
# string_without_space=String.replace(" ","")
# lower=0
# upper=0
#
# for i in string_without_space:
#       if(i.islower()):
#             lower+=1
#       else:
#             upper+=1
# print("The number of lowercase characters is:",lower)
# print("The number of uppercase characters is:",upper)

### Write a Python function to sum all the numbers in a list.
# numbers = (8,2,3,0,7)
# print (f"Sum: {sum(numbers)}")

### Write a Python function that checks whether a passed string is a palindrome or not.
