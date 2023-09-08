#---------------------------------------------variables and functions
import random

#Total number of rounds
numOfRounds = 1

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
    global compInput

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

#run until currentRound equal numOfRounds
while userWon < numOfRounds and userLost < numOfRounds:

    # control the userInput loop
    valid_input = False  

    while not valid_input:
        #gets users input and also turns it uppercase
        userInput = input("Rock, Paper or Scissors: ").upper()
        #checks if the input is valid
        if userInput == "ROCK" or userInput == "PAPER" or userInput == "SCISSORS":
            #exits the loop
            valid_input = True
        else:
            userInput = input("Your previous response was invalid. Try Again. Rock, Paper or Scissors: ")

    compSelection()

    #When computer's input is ROCK
    if compInput == 'ROCK' and userInput == 'PAPER':
        #user wins the round
        userWon = userWon + 1
        currentRound = currentRound + 1
        print('Computer: Rock')
        print('Player: PAPER')
    if compInput == 'ROCK' and userInput == 'SCISSORS' :
        #user loses the round
        userLost = userLost + 1
        currentRound = currentRound + 1
        print('Computer: Rock')
        print('Player: Scissors')
    if compInput == 'ROCK' and userInput == 'ROCK':
        #user and computer draw
        userDrew = userDrew + 1
        currentRound = currentRound + 1
        print('Computer: Rock')
        print('Player: Rock')

    #When computer's input is PAPER
    if compInput == 'PAPER' and userInput == 'SCISSORS':
        #user wins the round
        userWon = userWon + 1
        currentRound = currentRound + 1
        print('Computer: Paper')
        print('Player: Scissors')
    if compInput == 'PAPER' and userInput == 'ROCK':
        #user loses the round
        userLost = userLost + 1
        currentRound = currentRound + 1
        print('Computer: Paper')
        print('Player: Rock')
    if compInput == 'PAPER' and userInput == 'PAPER':
        #user and computer draw
        userDrew = userDrew + 1
        currentRound = currentRound + 1
        print('Computer: Paper')
        print('Player: Paper')

    #When computer's input is SCISSORS
    if compInput == 'SCISSORS' and userInput == 'ROCK':
        #user wins the round
        userWon = userWon + 1
        currentRound = currentRound + 1
        print('Computer: Scissors')
        print('Player: Rock')
    if compInput == 'SCISSORS' and userInput == 'PAPER':
        #user loses the round
        userLost = userLost + 1
        currentRound = currentRound + 1
        print('Computer: Scissors')
        print('Player: Paper')
    if compInput == 'SCISSORS' and userInput == 'SCISSORS':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Scissors')
        print('Player: Scissors')

#evaluating the results after all rounds are played
if userWon > userLost:
    print('You won the game!')
elif userLost > userWon:
    print('You lost the game.')
else:
    print('It\'s a tie.')

print('Rounds Won:', userWon, 'Rounds Lost:', userLost, 'Rounds Drew:', userDrew)
