import random

#Boolean var that shows the game is running
continueGame = True

#rounds user won, lost or drew
userWon = 0
userLost = 0
userDrew = 0

#function that generates and returns computers response
def compSelection():
    #num equal a random floating point number between 1 and 3, including 3
    num = random.randint(1,3)

    #if num = 1 then set the comp's value to ROCK
    if(num == 1):
        return 'ROCK'
    #if num = 2 then set the comp's value to PAPER
    elif(num == 2):
        return 'PAPER'
    #if num = 3 then set the comp's value to SCISSORS
    elif(num == 3):
        return 'SCISSORS'

#logic for each round 
def round(user,computer):
    global userWon
    global userLost
    global userDrew
    global continueGame

    userSelection = str(user)
    computerSelection = computer


    #When computer's input is ROCK
    if computerSelection == 'ROCK' and userSelection == 'PAPER':
        #user wins the round
        userWon = userWon + 1
        print('-----------------------------------------------------')
        print('Computer: Rock')
        print('Player: Paper')
        print('You win the round!')
        print('-----------------------------------------------------')
    if computerSelection == 'ROCK' and userSelection == 'SCISSORS' :
        #user loses the round
        userLost = userLost + 1
        print('-----------------------------------------------------')
        print('Computer: Rock')
        print('Player: Scissors')
        print('You lost the round')
        print('-----------------------------------------------------')
    if computerSelection == 'ROCK' and userSelection == 'ROCK':
        #user and computer draw
        userDrew = userDrew + 1
        print('-----------------------------------------------------')
        print('Computer: Rock')
        print('Player: Rock')
        print('It was a draw')
        print('-----------------------------------------------------')

    #When computer's input is PAPER
    if computerSelection == 'PAPER' and userSelection == 'SCISSORS':
        #user wins the round
        userWon = userWon + 1
        print('-----------------------------------------------------')
        print('Computer: Paper')
        print('Player: Scissors')
        print('You win the round!')
        print('-----------------------------------------------------')
    if computerSelection == 'PAPER' and userSelection == 'ROCK':
        #user loses the round
        userLost = userLost + 1
        print('-----------------------------------------------------')
        print('Computer: Paper')
        print('Player: Rock')
        print('You lost the round')
        print('-----------------------------------------------------')
    if computerSelection == 'PAPER' and userSelection == 'PAPER':
        #user and computer draw
        userDrew = userDrew + 1
        print('-----------------------------------------------------')
        print('Computer: Paper')
        print('Player: Paper')
        print('It was a draw')
        print('-----------------------------------------------------')

    #When computer's input is SCISSORS
    if computerSelection == 'SCISSORS' and userSelection == 'ROCK':
        #user wins the round
        userWon = userWon + 1
        print('-----------------------------------------------------')
        print('Computer: Scissors')
        print('Player: Rock')
        print('You win the round!')
        print('-----------------------------------------------------')
    if computerSelection == 'SCISSORS' and userSelection == 'PAPER':
        #user loses the round
        userLost = userLost + 1
        print('-----------------------------------------------------')
        print('Computer: Scissors')
        print('Player: Paper')
        print('You lost the round')
        print('-----------------------------------------------------')
    if computerSelection == 'SCISSORS' and userSelection == 'SCISSORS':
        #user and computer draw
        userDrew = userDrew + 1
        print('-----------------------------------------------------')
        print('Computer: Scissors')
        print('Player: Scissors')
        print('It was a draw')
        print('-----------------------------------------------------')
    
    if userWon == 2:
        print('You Win!')
        print('You won ', userWon, ' rounds,', 'You lost ', userLost, ' rounds,', 'You drew ', userDrew, ' rounds.')
        continueGame = False
        exit()
    if userLost == 2:
        print('You Lost!')
        print('You won ', userWon, ' rounds,', 'You lost ', userLost, ' rounds,', 'You drew ', userDrew, ' rounds.')
        continueGame = False
        exit()

#plays the game
def game(userSelection):
    round(userSelection, compSelection())

while continueGame == True:
    userResponse = input('Rock, Paper, Scissors: ').upper()
    game(userResponse)