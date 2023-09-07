#---------------------------------------------variables and functions
import random

#Total number of rounds
numOfRounds = 3

#current round
currentRound = 0

#Number of rounds user won & lost & drew
userWon = 0
userLost = 0
userDrew = 0

#---------------the computer's variables and functions

#contains the computers response
compInput = ''

#computer's response
def compSelection():
    #num equal a random floating point number between 1 and 3, including 3
    num = random.uniform(1,3)

    #if num = 1 then set the comp's value to ROCK
    if(num == 1):
        compInput = 'ROCK'
    #if num = 2 then set the comp's value to PAPER
    elif(num == 2):
        compInput = 'PAPER'
    #if num = 3 then set the comp's value to SCISSORS
    elif(num == 3):
        compInput = 'SCISSORS'


#contains the user's response 
userInput = input("Rock, Paper or Scissors: ")

#Turns every letter of user's response to uppercase -> its better for comparison
userInput = userInput.upper()

#Checking if the users response is valid
if userInput != "ROCK" | userInput != "PAPER" | userInput != "SCISSORS":
    #if its not valid -> ask to user for another response
    userInput = input("Your previous response was invalid, Try Again. Rock, Paper or Scissors")

#run until currentRound equal numOfRounds
while currentRound < numOfRounds:

    #When computer's input is ROCK
    if compInput == 'ROCK' & userInput == 'PAPER':
        #user wins the round
        userWon = userWon + 1
        print('Computer: Rock')
        print('Player: PAPER')
    if compInput == 'ROCK' & userInput == 'SCISSORS' :
        #user loses the round
        userLost = userLost + 1
        print('Computer: Rock')
        print('Player: Scissors')
    if compInput == 'ROCK' & userInput == 'ROCK':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Rock')
        print('Player: Rock')

    #When computer's input is PAPER
    if compInput == 'PAPER' & userInput == 'SCISSORS':
        #user wins the round
        userWon = userWon + 1
        print('Computer: Paper')
        print('Player: Scissors')
    if compInput == 'PAPER' & userInput == 'ROCK':
        #user loses the round
        userLost = userLost + 1
        print('Computer: Paper')
        print('Player: Rock')
    if compInput == 'PAPER' & userInput == 'PAPER':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Paper')
        print('Player: Paper')

    #When computer's input is SCISSORS
    if compInput == 'SCISSORS' & userInput == 'ROCK':
        #user wins the round
        userWon = userWon + 1
        print('Computer: Scissors')
        print('Player: Rock')
    if compInput == 'SCISSORS' & userInput == 'PAPER':
        #user loses the round
        userLost = userLost + 1
        print('Computer: Scissors')
        print('Player: Paper')
    if compInput == 'SCISSORS' & userInput == 'SCISSORS':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Scissors')
        print('Player: Scissors')