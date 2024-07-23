# Conditions in python
# Day 9 - 30 Days of Python Daily Coding Challenge

print("Introduction")
print("Day 9 - 30 Days of Python Daily Coding Challenge")
print("Start")

# if condition
print("If condition")
a = 3
if a > 0:
    print("A is a positive number")

# if else
print("if else")
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# if elif else
print("if elif else")
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
# short hand
print("short hand")
a = 3
# first condition met, 'A is positive' will be printed
print('A is positive') if a > 0 else print('A is negative')
# nested conditions
print("nested conditions")
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
# If Condition and Logical Operators
print("If Condition and Logical Operators")
a = 0
if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
# If and Or Logical Operators
print("If and Or Logical Operators")
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access granted!')
else:
    print('Access denied!')
print("End")
print("Thanks for watching")
