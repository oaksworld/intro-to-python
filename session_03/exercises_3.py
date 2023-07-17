# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

'''name = input("What is your name? ")

if name == 'Bob':
 print("Welcome " + name + "!") '''

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
'''
name2 = input("What is your name? ")
if name2 != "Alice":
  print("Your name is not Alice!") '''


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
'''  If they get it wrong, print "Password failure".
password = input("What is your password? ")
if password == "qwerty123":
  print("You have successfuly logged in")
else: print("Password Failure!") '''


# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
'''number = int(input("Enter a number: "))
if number % 2 == 0:
   print("Even")
else: print ("Odd") '''


# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
'''
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

if number2 & number3 >= 21:
  print("Bust")
else: print("Safe") '''

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

'''length = input("What is the length of the shape?")
width = input("What is the width of the shape?")
if length == width: 
  print("It is a sqaure")
else: print("It is not a sqaure") '''


# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

''' 
 sal = int(input("Enter your current salary: "))
 year = int(input("Enter your years of service: "))

if year > 3:
   print (str(sal + sal *0.1))
 else: print ("No Bonus!") '''

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
'''
 numero = int(input("Enter a number: "))
 if numero >0 :
 print(numero**3)
 else: print(numero/2) '''
  


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

'''name = input("What is your name?")
 if name == "Alice":
print '''

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

''' age = int(input("Enter your age: "))

if age <= 11: 
 print("You're too young to go to this school!")
  
 elif age >= 11 & age <= 16:
   print("You can come to this school")
  
 elif age == 0:
  print("You're not born yet!") '''


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

''' month = input("What is the name of the month: ")
if month == "March" or month == "April" or month == "May":
  print(month+ " is in Spring! ")
  
elif month == "June" or month == "July" or month == "August":
  print(month + " is in Summer!")
elif month == "September" or month == "October":
  print(month+ " is Winter!")
else:
    print("I don't know") 
'''

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

'''number1 = input("Enter a number: ")
number2 = input("Enter a number: ")

if (number1 % 2 == 0 and number2 % 2 == 0):
    print("Both numbers are even.")
elif (number1 % 2 == 1 and number2 % 2 == 1):
    print("Both numbers are odd.")
else:
    print(number1 * number2)'''

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

'''number_val = int(input("Enter a number: "))
number_val2 = int(input("Enter a number: "))

if number_val > number_val2:
  print(str(number_val) + " has the highest value")
else: 
  print(str(number_val2) + " has the highest value")'''

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.



# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.



# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
