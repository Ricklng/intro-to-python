# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
# name = input("What is your name? ")
# if name == ("Rick") :
#   print("Hello Rick")
#   print("Welcome to class")
# print( "You are not Rick") 
# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
# name = input("What is your name? ")
# if name != ("Alice") :
#   print("You are not Alice! ")
# else :
#   print("You are Alice!")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
# password = input("Please insert your password ")
# if password == ("qwerty123") :
#   print("You have successfully logged in ")
# else :
#   print("Password failure ")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
# number = int(input("Please enter a number "))
# result = number%2
# if result == 0 :
#   print("The number is even ")
# else:
#   print("The number is odd ")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
# number_1 = int(input("Please input number 1 "))
# number_2 = int(input("Please input number 2 "))
# blackjack = number_1 + number_2
# if blackjack > 21 :
#   print("Bust")
# else :
#   print("Safe")


# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
# length = int(input("Please input the length of a shape "))
# width = int(input("Please input the width of a shape "))

# if length == width :
#   print("The shape is a square ")
# else:
#   print("The shape is not a square ")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# years = int(input("How many years have you been with us? "))
# salary = float(input("How much is your current salary? "))
# bonus = 0.1 * salary
# if years > 3 :
#   print(0.1 * salary)
# else:
#   print("You are not eligible for bonus ")


# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
# number = int(input("Please input a number "))
# if number >= 0 :
#   print (number ** 3)
# else:
#   print(number * 0.5)
  



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

# name = input("What is your name? ")
# if name == ("Alice"):
#   print("Hello Alice! ")
# elif name == ("Bob") :
#   print("Hello Bob! ")
# else:
#   print("You must be Charlie ")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
# age = int(input("How old are you? "))
# if age == 0:
#   print("You're not born yet ")
# elif age < 11:
#   print("You're too young to go to this school ")
# elif age >= 11 and age <= 16 :
#   print("You can come to this school ")
# elif age > 16:
#   print("You are too old for school ")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
# month = input(("What month are we in? "))
# if month == ("March") or month == ("April") or month == ("May"):
#   print( month + (" is in Spring "))
# if month == ("June") or month ==  ("July") or month == ("August"):
#   print( month + (" is in Summer "))
# elif month == ("September") or month == ("October") or month == ("November"):
#   print( month + (" is in Autumn "))
# elif month == ("December") or month == ("January") or month == ("February"):
#   print( month + (" is in Winter "))
# else:
#   print(" I dont know ")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
# num1 = int(input("Please input a number: "))
# num2 = int(input("Please input another number: "))
# if num1%2 == 0 and num2%2 == 0:
#   print("Even")
# elif num1%2 > 0 and num2%2 > 0:
#   print("Odd")
# else :
#   print(num1 * num2)



# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
# num1 = int(input("Please input a number: "))
# num2 = int(input("Please input another number: "))
# if num1 > num2 :
#   print("The hightest number is " + str(num1))
# else:
#   print("The hightest number is " + str(num2))


# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# salary = float(input("How much do you earn? "))
# service = int(input("How long have you been with us? "))
# if service >= 3 and service <= 5:
#   print("Your salary is " + str(salary)+ " and your bonus is " +  str(0.1 * salary))
# elif service > 5 and service <7:
#   print("Your salary is " + str(salary)+ " and your bonus is " +  str(0.15 * salary))
# elif service >= 7:
#   print("Your salary is " + str(salary) + " and your bonus is " +  str(0.2 * salary))
# else:
#   print ("Since your years of service is less than three, you are ineligible for bonus this year")



# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
sum = 5 + 6
if sum == 10:
  print("the value is 10")



# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
# lesson1 = input("Input name of first lesson: ")
# grade1 = int(input("Input grade of " + lesson1 + ": " ))
# lesson2 = input("Input name of seccond lesson: ")
# grade2 = int(input("Input grade of " + lesson2 + ": " ))
# lesson3 = input("Input name of third lesson: ")
# grade3 = int(input("Input grade of " + lesson3 + ": " ))
# if grade1 < 25:
#   print("Grade for " + str(lesson1) + " is F")
# elif  grade1 >=25 and grade1 <= 45:
#   print("Grade for " + str(lesson1) + " is E")
# elif  grade1 >45 and grade1 <= 50:
#   print("Grade for " + str(lesson1) + " is D")
# elif  grade1 >50 and grade1 <= 60:
#   print("Grade for " + str(lesson1) + " is C")
# elif  grade1 >60 and grade1 <= 80:
#   print("Grade for " + str(lesson1) + " is B")
# else:
#   print("Grade for " + str(lesson1) + " is A")
# if grade2 < 25:
#   print("Grade for " + str(lesson2) + " is F")
# elif  grade2 >=25 and grade2 <= 45:
#   print("Grade for " + str(lesson2) + " is E")
# elif  grade2 >45 and grade2 <= 50:
#   print("Grade for " + str(lesson2) + " is D")
# elif  grade2 >50 and grade2 <= 60:
#   print("Grade for " + str(lesson2) + " is C")
# elif  grade2 >60 and grade2 <= 80:
#   print("Grade for " + str(lesson2) + " is B")
# else:
#   print("Grade for " + str(lesson2) + " is A")
# if grade3 < 25:
#   print("Grade for " + str(lesson3) + " is F")
# elif  grade3 >=25 and grade3 <= 45 :
#   print("Grade for " + str(lesson3) + " is E")
# elif  grade3 >45 and grade3 <= 50:
#   print("Grade for " + str(lesson3) + " is D")
# elif  grade3 >50 and grade3 <= 60:
#   print("Grade for " + str(lesson3) + " is C")
# elif  grade3 >60 and grade3 <= 80:
#   print("Grade for " + str(lesson3) + " is B")
# else:
#   print("Grade for " + str(lesson3) + " is A")