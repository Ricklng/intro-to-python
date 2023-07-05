# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
# import random
# for number in range(10):
#   print(random.randint(1,10))


  


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
# guess = None
# while guess != 7:
#   guess = int(input("What's your number? "))

# print("Wow lucky number 7! ")
# import random
# cpu = random.randint(1, 10)
# guess = None
# while cpu != guess:
#   guess = int(input("Guess the lucky number :\n"))
# print("Well done!! ")


# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
# import math
# width = int(input("What is the width in cm? "))
# height = int(input("What is the height in cm? "))
# area_cm = width * height
# area_m = math.ceil(area_cm / 10000)
# print("The area in metres square is " +  str(area_m))


# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
# user = input("What is your password? \n")
# password = "qwerty123"
# user_guesses = 0
# while user_guesses < 2:
#   if user == password:
#     print("You have successfully logged in ")
#     break
#   else:
#     print("PASSWORD FAILURE \n")
#     user = input("What is your password? \n")
#     user_guesses +=1
# if user_guesses == 2:
#   print("PASSWORD FAILURE \n")
#   print("PROFILE LOCKED!! You have entered 3 incorrect passwords ")

# 5. Add up all the numbers from 1 to 500 and print the answer.
# number = range(1,501)
# sum = 0 
# for  i in number:
#   sum += i
# print(sum)
  

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
# num_list = []
# numbers = ""
# i = 0
# x = 0 
# print("Pick 10 numbers, one of those numbers must be 99")

# while i < 10:
#   numbers = int(input("Pick a number:\n"))
#   num_list.append(numbers)
#   i += 1 

# while x < len(num_list):
#   if num_list[x] == 99:
#     print("Number 99 is at index " + str(x))
#   x += 1

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 3
# i = 1
# while i < 16:
#   print(str(i) + " x 18 = " + str(i*18))
#   i +=1
  
# import random
# number = 0 
# while number <= 4:
#   print(random.randint(1,10))
#   number +=1


# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
# i = 1
# while i <101: 
#   print(i)
#   i+=1


# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

# lesson = 0

# print("REPORT CARD:")

# while lesson < 3:
#     lesson = input("Input your lesson:\n")
#     mark = int(input("Input your mark:\n"))
#     if mark > 80:
#         print(lesson + " - A grade")
#     elif mark <= 80 and mark > 60:
#         print(lesson + " - B grade")
#     elif mark <= 60 and mark > 50:
#         print(lesson + " - C grade")
#     elif mark <= 50 and mark> 45:
#         print(lesson + " - D grade")
#     elif mark <= 45 and mark > 25:
#         print(lesson + " - E grade")
#     elif mark < 25:
#         print(lesson + " - F grade")
#     else:
#         print("Go to see your teacher")
# lesson += 1

# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
# import random
# winner = []
# i = 0 
# while i < 6:
#   user = input("Please input a random name \n")
#   winner.append(user)
#   i+=1
# print("The random winner is " + random.choice(winner))
  


# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
# import random

# print("Welcome to Rock, Paper, Scissors")

# user_score = 0
# computer_score = 0
# turns = 0

# while turns < 3:
#   user_choice = input("What is your move? (rock, paper, scissors) ")
#   computer_choice = random.choice(["rock", "paper", "scissors"])
#   print("You picked " + user_choice)
#   print("The computer picked " + computer_choice)
#   turns += 1
#   print("This is turn: " + str(turns))
#   if user_choice == "rock":
#       if computer_choice == "scissors":
#           print("You Win")
#           user_score += 1
#       elif computer_choice == "paper":
#           print("You Lose")
#           computer_score += 1
#       else:
#           print("It's a draw")
#   elif user_choice == "paper":
#       if computer_choice == "rock":
#           print("You Win")
#           user_score += 1
#       elif computer_choice == "scissors":
#           print("You Lose")
#           computer_score += 1
#       else:
#           print("It's a draw")
#   else:
#       if computer_choice == "paper":
#           print("You Win")
#           user_score += 1
#       elif computer_choice == "rock":
#           print("You Lose")
#           computer_score += 1
#       else:
#           print("It's a draw")

# print("Game Over! Final Score: User Score: " + str(user_score) + "\n Computer Score: " + str(computer_score)) 
# time = 0
# while time >= 0:
#   print("Hello")
#   time += 1
#   if time >5:
#     break