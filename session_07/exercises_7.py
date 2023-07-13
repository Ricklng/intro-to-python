# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
# def name():
#   print("Oluchukwu ")
# name()


# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
# def hello(name):
#   print("Hello, " + name )

# hello("Rick")
# hello("Cynthia")
# hello("Arahmac")


# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the funct2ion you just wrote.
# names = ["Alice", "Bob", "Charlie"]
# def hello(name):
#   print("Good Morning, " + name)

# for name in names:
#   hello(name)

# 4. Write a function that prints the area of two passed in parameters.
# def area(x,y):
#   print("The area is " + str(x * y))

# area(4,7)
# area(35,57)

# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
# def print_list(fruits):
#   for fruit in fruits:
#     print(fruit)

# print_list(["Oranges", "Guava", "Pineapple"])


# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

# def school_eligibility(age):
#   if age < 11:
#     print("You are too young to go to this school.")
#   elif age >=11 and age <= 16:
#     print("You can come to this school. ")
#   elif age > 16:
#     print("You are too old for school.")
#   elif age == 0:
#     print("You are not born yet. ")
#   else:
#     print("You didn't pick a number.")

# school_eligibility (17)
# school_eligibility(0)
# school_eligibility(25)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# is_odd(6)
# is_odd(5)

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
def reverse_word(name):
  new_string = ""
  name_length = len(name)
  while name_length != 0:
    name_length -=1
    new_string += name[name_length]
  return new_string

reverse_word("The Explorers")

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```



# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".



# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.



# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.



# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.



# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
