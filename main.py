#Write a Python program to create a calculator. Create individual 
# functions for different operators - addition, subtraction, division, 
# multiplication and return the output value.
def add(a,b):
    print(a+b)
def substrac(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
number=int(input("Please enter a number:"))
number2=int(input("Please enter a number:"))
add(number,number2)
substrac(number,number2)
multiply(number,number2)
divide(number,number2)

