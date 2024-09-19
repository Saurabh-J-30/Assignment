### Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.
# A = 1
# B = 1.0
# C = '1'
# print ("A:" ,A, 'Type:', type(A), "B:" ,B, 'Type:', type(B), "C:" ,C, 'Type:', type(C))


### Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.

# A = A + 1
# B = B + 1
# C = int(C)
# C = C + 1
# C = str(C)
# print ("A:" ,A, 'Type:', type(A), "B:" ,B, 'Type:', type(B), "C:" ,C, 'Type:', type(C))


### Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c.

# A=B=C=D=10
# print ("A: ",A, "B: ",B, "C: ",C, "D: ",D)


### Assign two variables a and b as integer and print the sum of a+b.

# A = 8
# B = 10
# print ("Sum:" ,A+B)

### Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?

# Fruits = ["apple", "banana", "cherry", "date", "strawberry"]
# print (Fruits)

### How do you access the second and fourth elements from the list.

# print (Fruits[1], Fruits[3])

### Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.

# Numbers = [10,20,30,40,50]
# Numbers[2] = 35
# print (Numbers)

### How do you create a tuple with the following elements: "red", "green", "blue"?

# colors = ('Red', 'Green', 'Blue')
# print (colors)


### How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?


# colors_1 = colors + tuple(('Yellow' ,'Orange'))
# print (colors_1)
# first_element = colors_1[0]
# last_element = colors_1[-1]
# print("First Element:", first_element)
# print("Last Element:", last_element)


### Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.

# Numbers = (10,20,30)
# (x,y,z) = Numbers
# print (x,y,z)
# print (type(Numbers))
# print (x)
# print (y)
# print (z)

### Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").

# color_present = 'Blue'
# exist = color_present in colors
# print (exist)

### Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").

# days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
# print (days)
# print (len(days))


### Create a dictionary where the keys are student names and the values are their grades.

# Student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print (Student_grades.keys())
# print (Student_grades.values())

### How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?

# print (Student_grades['Bob'])

### Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.

# Student_grades.update ({"David": 92})
# del Student_grades ["Charlie"]
# print("Updated Student_grades is:", Student_grades)

### Write a Python program to update Bob's grade to 95 in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

# Student_grades["Bob"] = 95
# print("Updated Student_grades is:", Student_grades)

### Write a Python program to check if "Alice" is a key in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

# if 'Alice' in Student_grades: print("Alice grades are present")
# else: print ("Alice grades are not present")

# if 'Alice' in Student_grades: print("Alice grades are:" ,Student_grades['Alice'])
# else: print ("Alice grades are not present")

### Write a Python program to find the number of key-value pairs in the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}.

# print (len(Student_grades))



