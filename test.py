def round(user,computer):

    userSelection = user.upper()
    computerSelection = computer.upper()


    #When computer's input is ROCK
    if computerSelection == 'ROCK' and userSelection == 'PAPER':
        #user wins the round
        userWon = userWon + 1
        print('Computer: Rock')
        print('Player: PAPER')
    if computerSelection == 'ROCK' and userSelection == 'SCISSORS' :
        #user loses the round
        userLost = userLost + 1
        print('Computer: Rock')
        print('Player: Scissors')
    if computerSelection == 'ROCK' and userSelection == 'ROCK':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Rock')
        print('Player: Rock')

    #When computer's input is PAPER
    if computerSelection == 'PAPER' and userSelection == 'SCISSORS':
        #user wins the round
        userWon = userWon + 1
        print('Computer: Paper')
        print('Player: Scissors')
    if computerSelection == 'PAPER' and userSelection == 'ROCK':
        #user loses the round
        userLost = userLost + 1
        print('Computer: Paper')
        print('Player: Rock')
    if computerSelection == 'PAPER' and userSelection == 'PAPER':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Paper')
        print('Player: Paper')

    #When computer's input is SCISSORS
    if computerSelection == 'SCISSORS' and userSelection == 'ROCK':
        #user wins the round
        userWon = userWon + 1
        print('Computer: Scissors')
        print('Player: Rock')
    if computerSelection == 'SCISSORS' and userSelection == 'PAPER':
        #user loses the round
        userLost = userLost + 1
        print('Computer: Scissors')
        print('Player: Paper')
    if computerSelection == 'SCISSORS' and userSelection == 'SCISSORS':
        #user and computer draw
        userDrew = userDrew + 1
        print('Computer: Scissors')
        print('Player: Scissors')

    
