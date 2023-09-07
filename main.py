#---------------------------------------------variables and functions
import random

#Ask the user the number of rounds that want to play
numOfRounds = input('Maximum number of rounds - 10, How many rounds do you want to play: ')

#Checking if the number of rounds is not too many
if numOfRounds > 10:
    numOfRounds = input('Maximum number of rounds - 10, How many rounds do you want to play: ')

#Number of rounds user won & lost & drew
userWon = 0
userLost = 0
userDrew = 0

#---------------the computer's variables and functions

#contains the computers response
comp = ''

#computer's response
def compSelection():
    #num equal a random floating point number between 1 and 3, including 3
    num = random.uniform(1,3)

    #if num = 1 then set the comp's value to ROCK
    if(num == 1):
        comp = 'ROCK'
    #if num = 2 then set the comp's value to PAPER
    elif(num == 2):
        comp = 'PAPER'
    #if num = 3 then set the comp's value to SCISSORS
    elif(num == 3):
        comp = 'SCISSORS'


#contains the user's response 
user = input("Rock, Paper or Scissors: ")

#Turns every letter of user's response to uppercase -> its better for comparison
user = user.upper()

#Checking if the users response is valid
if(user != "ROCK" | user != "PAPER" | user != "SCISSORS"):
    #if its not valid -> ask to user for another response
    user = input("Your previous response was invalid, Try Again. Rock, Paper or Scissors")
