# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

width = 7
height = 8
area = width * height
print("Rectangle of width " + str(width) + " and height " + str(height) + " has an area of "+ str(area) + ".")

# 2. Write code that prints the length of the string, 'python'.
name = "python"
name_length = print(len(name))


# 3. Print out the first and third letter of the word 'python'.

name1 = "python"
print(name1[0])
print(name1[5])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.

# name2 = input("What is your name? ")
# print ("Hello " + name2 )

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

# age = int(input("What is your age?"))
# print ("Your age in 15 years will be " + str(age + 15) + ".")

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

# nameAgain = input("What is your name?")
# current_age = int(input("What is your age?"))

# print("Hello " + nameAgain + ". You are currently aged " + str(current_age) + " years old.")
# print("In 15 years time you will be " + str(current_age + 15) + " years old.")





# 7. Ask the user to enter their hometown, print it out in uppercase letters.

# HomeTown = input("What is your hometown?")
# print (HomeTown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

# FavColour = input("What is your favourite colour?")
# print (len(FavColour))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

# WeatherToday = input("What is the weather like today?")
# MonthToday = input ("What month are we in?")
# print ("It is " + WeatherToday + "")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

month = input("What is the month? ")
temp0 = int(input("Enter a temp: "))
temp1 = int(input("Enter a temp: "))
temp2 = int(input("Enter a temp: "))
temp3 = int(input("Enter a temp: "))
temp4 = int(input("Enter a temp: "))

# average_temp = (temp0 + temp1 + temp2 + temp3 + temp4)/5

# Print out the whole string, not forgetting to cast the integer values to strings
# print("It is " + month + " and the average temperature is " + str(average_temp) + " degrees celsius.")


# 11. Print out the above sentence but make the month upper case.

# print("It is " + month.upper() + " and the average temperature is " + str(average_temp) + " degrees celsius.")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
#  fav_animals = "My favourite animals are:\n\tKoala Bears,\n\tElephants,\n\tWhales,\n\tHorses,\n\tLion"

# Print the list out
#  print(fav_animals)


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.

# Ask the user for input
name = input("What is your name?")
number = int(input("Pick a number"))

#?????

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".

str = "WelcometoPython"
print(len(str))
print(str[1:14:2])