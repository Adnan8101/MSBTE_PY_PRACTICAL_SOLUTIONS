"""Write simple Python program using operators:
a) Arithmetic Operators
b) Logical Operators
c) Bitwise Operators
 """

# a) Arithmetic Operators
num1 = int(input("Enter first the numbers"))
num2 = int(input("Enter second the numbers"))
print("Addition of both the number is ", num1 + num2)
print("Subraction of both the number is ", num1 - num2)
print("Division  of both the number is ", num1 / num2)
print(" Multiplication  of both the number is ", num1 * num2)
print("Exponential  of both the number is ", num1 ** num2)
print("Modulus of both the number is", num1 % num2)

# B  Logical Operators
num1 = 10
num2 = 20

# using 'and' logical operator
if num1 > 0 and num2 > 0:
    print("Both numbers are positive")

# using 'or' logical operator
if num1 > 0 or num2 > 0:
    print("At least one of the numbers is positive")
# using 'not' logical operator
if not(num1 < num2): # use ' < ' / '== ' to understand properly
    print("Not Logical operator executed")

# Bitwise operators
# Program to calculate the binary product of two numbers

a = 4
b = 5

# Using bitwise operators
# To calculate the binary product
result = a & b

print("The binary product of", a,"and", b, "is", result)
