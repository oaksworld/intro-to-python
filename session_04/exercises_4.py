# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

fruits = ['Apples', 'Cherries', 'Pears', 'Pineabpple', 'Peaches', 'Mango']
print(fruits)

# 2. Add "Grapes" to the list and print the list.

fruits.append('Grapes')
print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.

fruits[2] = 'Strawberries'
print(fruits)

# 4. Remove "Apples" from the list and print the list.

del(fruits[0])
print(fruits)

# 5. Print out the current length of the list.

print(len(fruits))

# 6. Order the list alphabetically.

fruits.sort()

# 7. Print out the list again.

print(fruits)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

for items in fruits:
  print(fruits)

# 2. Print the numbers 1 to 100 (including the number 100).

'''for items in range (1,101):
  print(items) '''

# 3. Print all odd numbers from 1 to 100.
for i in range(1, 101):
    if i % 2:
        print(i)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

for olympic_year in range(1896, 2022, 4):
    print(olympic_year)

# Bonus: skip the years it has not been 1916, 1940, 1944, 2020

not_held = [1916, 1940, 1944, 2020]

for olympic_year in range(1896, 2022, 4):
    if olympic_year not in not_held:
        print(olympic_year)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.

numbers = [1, 10, 13 , 15, 765, 32, 65, 23, 56, 101]
even_count = 0
odd_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        # This is short hand for the line above
        odd_count += 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
names = ['Stacey', 'Monday', 'Gina', 'Bob', 'Tracy']
for items in names:
  print ("Hello, " + items)


# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

word = "supercalifragilisticexpialidocious"

for i in word:
    print(i)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
numbers = [2, 5, 8, 9, 10]
sqr_numbers = []

for i in numbers:
    sqr_numbers.append(i ** 2)

print(sqr_numbers)


# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.


namess = ['Stacey', 'London', 'Zaida', 'Honey', 'Bella']
for items in namess:
  print ("Dr " + items)

names = ["Saf", "Graham", "Jake", "Sanj", "Fis"]
drs = []
for name in names:
    drs.append("Dr. " + name)
print(drs)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```



for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
  