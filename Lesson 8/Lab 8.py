'''

This project uses the random module in Python. The program will first randomly 
generate a number unknown to the user. The user needs to guess what that number is. 
(In other words, the user needs to be able to input information.) If the user’s guess 
is wrong, the program should return some sort of indication as to how wrong (e.g. The 
number is too high or too low). If the user guesses correctly, a positive indication 
should appear. You’ll need functions to check if the user input is an actual number, 
to see the difference between the inputted number and the randonly generated numbers, 
and to then compare the numbers.

'''

import random

def GetRandomNumber():
    return random.randint(1,101)

def CompareNumbers(randNumber, userNumber):
    return userNumber - randNumber

# Step 1 - Get random number.
randNumber = GetRandomNumber()

keepGoing = True

while(keepGoing):
    
    # Step 2 - Ask user for number.
    userNumber = input("Please choose a number between 1 and 100: ")

    # Step 2.5 - Change to integer.
    try:
        intUserNumber = int(userNumber)
    except:
        print("Please try again with a number.")
        continue

    # Step 3 - Compare numbers.
    difference = CompareNumbers(randNumber, intUserNumber)

    print(str(randNumber) + " " + str(userNumber))

    # Step 4 - Give user feedback.
    if difference < 0:
        print("Your choice is too low.")
    elif difference > 0:
        print("Your choice is too high.")
    else:
        print("Your choice is correct.")
        keepGoing = False
          
print("Game Over. Congratulations!")





