# Rock-Paper-Scissors

# create a player input function
def playerone():
    print('Hi, player 1. Please choose one from Rock-paper-scissors.')
    player1 = 0
    while player1 not in ['rock','scissors','paper']:
        
        print('Please type "rock", "paper", or "scissors"')
        player1 = input()
    return player1

def playertwo():
    print('Hi, player 2. Please choose one from Rock-paper-scissors.')
    player2 = 0
    while player2 not in ['rock','scissors','paper']:
        
        print('Please type "rock", "paper", or "scissors"')
        player2 = input()
    return player2
        
# create a compare function
def compare(p1,p2):
    if p1 == 'rock' and p2 == 'rock':
        print('Draw!')
    if p1 == 'scissors' and p2 == 'scissors':
        print('Draw!')
    if p1 == 'paper' and p2 == 'paper':
        print('Draw!')
    if p1 == 'rock' and p2 == 'scissors':
        print('Player 1 beats player 2!')
    if p1 == 'rock' and p2 == 'paper':
        print('Player 2 beats player 1!')
    if p1 == 'scissors' and p2 == 'rock':
        print('Player 2 beats player 1!')
    if p1 == 'scissors' and p2 == 'paper':
        print('Player 1 beats player 2!')
    if p1 == 'paper' and p2 == 'rock':
        print('Player 1 beats player 2!')
    if p1 == 'paper' and p2 == 'scissors':
        print('Player 2 beats player 1!')

play_again = True

while play_again:
    player1 = playerone()
    player2 = playertwo()
    compare(player1, player2)
    print('Do you want to play again? y or n')
    again = input()
    if again == 'n':
        play_again = False




