"""
 Write simple Python program to demonstrate use of conditional statements:
a) 'if statement
b) 'if ... else' statement
c) Nested ' i f statement
 """
# 'if statement
num = int(input("Enter any number :"))
if num > 0:
    print("The given number is postive number")
else:
    print("Number is Negative number")

# 'if ... else' statement
marks = int(input("Enter your total percentage , without using '%' : "))
if marks > 90 and marks < 100:
    print("You score A+ Grade")
elif marks > 80 and marks < 90:
    print("You score A Grade")
elif 70 < marks < 80:
    print("You score B+ Grade")
elif 60 < marks < 70:
    print("You score B Grade")
elif marks > 50 and marks < 40:
    print("You score C Grade")
else:
    print("You have faided this Semester")

# Nested if statement
a = 15

if a > 10:
   if a == 15:
      print("a is 15")
   else:
      print("a is not 15")
else:
   print("a is not greater than 10")
