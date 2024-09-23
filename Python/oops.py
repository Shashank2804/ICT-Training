# class human:
#     #constructor method to inisilise the attributes
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"age: {self.age}")
#         print(f"Address: {self.address}")
# #creating the object
# shashank = human(name="Shashank",age=30,address="Bangalore")
# nithya = human(name="Nithya",age=22,address="KR Puram")
# manisha = human(name="Manisha",age=23,address="Yelanka")

# shashank.display_info()
# nithya.display_info()
# manisha.display_info()

# #Inheritance
# class Animal:
#     def speak(self):
#         print('Animal speakes')
# class Dog(Animal):
#     def barks(self):
#         print('It barks')
# d = Dog()
# d.speak()#inherited method 
# d.barks()#own method

#multlevel inheritances
# class Animal:
#     def sleep(self):
#         print('Animal can sleep')
# class Mammal(Animal):
#     def walk(self):
#         print('Mammales can walk')
# class Dog(Mammal):
#     def bark(self):
#         print('Dog can Bark')
# d = Dog()
# d.sleep()
# d.walk()
# d.bark()

#heirarchial inheritances =multiple derived class inherite from single base class
# class Animal:
#     def speak(self):
#         print('Animal speakes')
# class Dog(Animal):
#     def barks(self):
#         print('It barks')
# class Cat(Animal):
#     def meow(self):
#         print('It mewos')
# d = Dog()
# d.speak()
# d.barks()

# d = Cat()
# d.speak()
# d.meow()

#super() function allows child class to inherit all methods and propertices from its parent class

# class Animal:
#     def __init__(self,name):
#         self.name = name
#         print(f"Animal name {self.name} created")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__("German Shepherd")
#         self.name = name
#         self.breed = breed
#         print(f"Dog name {self.name} of breed {self.breed} created")

# animal = Animal('Generic Animal')
# dog = Dog("Buddy","GOLDEN RETERVER")

# class Parent:
#     def __init__(self):
#         print("Parent init")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child init")

# c = Child()

# with the Function overloading example
# class Dog:
#     def speak(self,sound=None):
#         if sound is None:
#             print('Dog Barks')
#         else:
#             print(f'Dog says {sound}')
# dog = Dog()
# dog.speak()
# dog.speak("Boww")

# from multipledispatch import dispatch

# @dispatch(int,int)
# def product(first,second):
#     result = first * second
#     print(result)
# product(2,3)

# @dispatch(int,int,int)
# def product(first,second,third):
#     result = first * second * third
#     print(result)
# product(2,3,4)

# @dispatch(float,float,float)
# def product(first,second,third):
#     result = first * second * third
#     print(result)
# product(2.2,3.4,2.3)

# class Point:
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y

#     def __mul__(self,other):
#         return Point(self.x*other.x,self.y*other.y)
    
#     def __truediv__(self,other):
#         return Point(self.x/other.x,self.y/other.y)
    
#     def __str__(self):
#         return (f"{self.x},{self.y}")
    
# point1 = Point(1,2)
# point2 = Point(3,4)

# result_mul = point1*point2
# print(f"Multiplication: {result_mul}")

# result_div = point1/point2
# print(f"Division: {result_div}")
    

# from multipledispatch import dispatch

# # Base class Person
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'Person(name={self.name})'

# # Derived class Student
# class Student(Person):
#     def __init__(self, name):
#         super().__init__(name)
#         self.skills = {}

#     @dispatch(str)
#     def add_skill(self, skill):
#         """Add a single skill."""
#         self.skills[skill] = 'Not Specified'
    
#     @dispatch(list)
#     def add_skill(self, skills):
#         """Add multiple skills."""
#         for skill in skills:
#             self.skills[skill] = 'Not Specified'
    
#     @dispatch(dict)
#     def add_skill(self, skills_proficiency):
#         """Add skills with proficiency levels."""
#         for skill, proficiency in skills_proficiency.items():
#             self.skills[skill] = proficiency

#     def __str__(self):
#         skills_str = ', '.join(f'{skill}: {proficiency}' for skill, proficiency in self.skills.items())
#         return f'Student(name={self.name}, skills={{ {skills_str} }})'

# # Example usage
# if __name__ == "__main__":
#     student = Student("Alice")
    
#     student.add_skill("Python")
#     student.add_skill(["Java", "C++"])
#     student.add_skill({"JavaScript": "Intermediate", "SQL": "Advanced"})

#     print(student)

# Reads the text in the text file 
# f = open("input.txt")
# print(f.read())

# rewrite the text
# f = open("input.txt","w")
# data = "Hello Students"
# f.write(data)

# Reads the text in the file
# file = open("input.txt","r")
# content = file.read()
# print(content)

# Reading the first 5 characters only
# f = open("input.txt")
# print(f.read(5))

# read() fun without any argument reads and return entire content
# with open("input.txt","rb") as file:
#     content = file.read()
#     print(content)

# The read() function reads from the current file pointer position. Here, file.seek() is used to move the pointer.
# with open("input.txt","r") as file:
#     file.seek(5)
#     content = file.read(31)
#     print(content)

# The readline() function reads a single line from the file each time it is called.
# with open("input.txt","r") as file:
#     line = file.readline()
#     while line:
#         print(line.strip()) #to remove newline characters
#         line = file.readline()

# The readlines() reads all the lines and returns a list of lines.
# with open("input.txt","r") as file:
#     #read all lines into list
#     lines = file.readlines()
#     print(f"Enter the file data: {lines}")
#     #print each line
#     for line in lines:
#         print(line.strip()) #to remove newline characters

# Write and Read Mode ('w+')
# with open('input.txt','w+') as file:
#     file.write("Writing about Darshan. \n")
#     file.seek(0)
#     content = file.read()
#     print(content)

# Binary Append and Read Mode ('ab+')
# with open('input.txt','ab+') as file:
#     file.write(b"Writing about ammu. \n")
#     file.seek(0)
#     content = file.read()
#     print(content)

     #Shallow Copy
# import copy
# original = [[1,2,3],[4,5,6]]
# shallow = copy.copy(original)
# original[0][2] = 100
# print(original)
# print(shallow)
    
# Deep copy
# import copy
# original = [[1,2,3],[4,5,6]]
# deep = copy.deepcopy(original)
# original[0][0] = 100
# print(original)
# print(deep)

# Return an iterator from a list, and print each value:
# city = ['Mumbai','Shanghai','Newyork','Tokey','Sydney']
# city = iter(city)
# print(next(city))
# print(next(city))
# print(next(city))
# print(next(city))
# print(next(city))

# Strings are also iterable objects, containing a sequence of characters:
# country = "INDIA"
# myit = iter(country)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# Iterator Example
# class Counter:
#     def __init__(self, low, high):
#         self.current = low
#         self.high = high

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.high:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1
     
# counter = Counter(1,5)
# for number in counter:
#     print(number)

#Create Fibonacci series using generator.
# def fibonacci(n):
#     a,b = 0,1
#     while a<n:
#         yield a 
#         a,b = b,a+b
# fib = fibonacci(10)
# for num in fib:
#     print(num)

# Create a decorator function that logs when say_hello() is called.
# def mydecorator(func):
#   def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#   return wrapper
# @mydecorator
# def say_hello():
#     print("Hello!")
# say_hello()

# The factorial of a positive integer 𝑛 is the product of all positive integers less than or equal to 𝑛. 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(10))

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "shashankmanjula2003@gmail.com"
receiver_email = "gsd99689@gmail.com"
# password = "$hashank@"
password = "itgoewspabgjlasz"
subject = "Test Email"
body = "This is a test email sent from Python"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
#Attach the body with msg instance
message.attach(MIMEText(body,"plain"))

#step3-Setup the SMTP server
smtp_server = "smtp.gmail.com"
port = 587
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() #secure the connection
    #login to the email account
    server.login(sender_email,password)
    #send the mail
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email successfully sent")
except Exception as e:
    print(f"error: {e}")
finally:
    server.quit() #close the connection
