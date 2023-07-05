# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

fruits = ["Apples", "Cherries", "Pears", "Pineapples", "Peaches", "Mango"]
# print(fruits)

# 2. Add "Grapes" to the list and print the list.
# fruits.append("Grapes")
# print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.
# fruits[2] = "Strawberries"
# print(fruits)

# 4. Remove "Apples" from the list and print the list.
# del(fruits[0])
# print(fruits)


# 5. Print out the current length of the list.
# print(len(fruits))


# 6. Order the list alphabetically.
# fruits.sort()
# print(fruits)


# 7. Print out the list again.
# print(fruits)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
# for items in fruits:
#   print(items)


# 2. Print the numbers 1 to 100 (including the number 100).
# for numbers in range(1,101):
#   print(numbers)


# 3. Print all odd numbers from 1 to 100.
# for numbers in range (1,100,2):
#   print(numbers)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
# not_held = [1916,1940, 1944, 2020]

# for years in range(1896,2024,4):
#   if years not in not_held:
#     print(years)




# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
# numbers = [2,15,84,96,0,54,73,81,99,10004]
# even_count = 0
# odd_count = 0
# for items in numbers:
#   if items % 2 == 0:
#     even_count += 1
#   else:
#     odd_count += 1
# print(even_count)
# print(odd_count)
# print("The amount of even number is " + str(even_count) +", while the amount of odd number is " + str(odd_count) )

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
# names = ["Rick", "Nenye", "Arams", "Jennifer", "Cynthia"]
# for items in names:
#   print("Hello " + items)


# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
# word = "supercalifragilisticexpialidocious"
# for letter in word:
#   print(letter)


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
# numbers = [2,3,4,5,6]
# squares = []

# for items in numbers:
#   squares.append(items ** 2)
# print(squares)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
# name1 =["Arams", "JennyBaby", "CynthiaDD", "Rick"]
# name2 = []
# for items in name1:
#   name2.append("Dr " + items)
# print(name2)
# total = 0
# for num in range(1,4):
#   total = total + num
# print(total)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".
# for number in range (1,101):
#   if (number % 3 == 0) and (number % 5 == 0):
#     print("FizzBuzz")
#   elif (number % 3 == 0):
#     print("Fizz")
#   elif(number % 5 == 0):
#     print ("Buzz")
#   else:
#     print(number)



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
