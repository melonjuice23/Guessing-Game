#Displays the board
import os
import random

def display_board(board):
    os.system('cls')
    
    print(board[1]+ '|'+ board[2]+'|'+board[3])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[7]+'|'+board[8]+'|'+board[9])

#Player input function
def player_input():
    
    marker = 'Wrong'
    
    while marker not in ['X','O']:
        
        marker = input("Player 1, pick a maker (X or O): ")
        marker = marker.upper()
    
    Player1 = marker
        
    if Player1 == 'X':
        
        Player2 = 'O'
    
    else:
        
        Player2 = 'X'
                
    return (Player1,Player2)


#Place marker on board
def place_marker(board, marker, position):
    board[position] = marker

#Checks if you win
def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or #Top Row
    (board[4] == board[5] == board[6] == marker) or #Middle Row
    (board[7] == board[8] == board[9] == marker) or #Bottom Row
    (board[1] == board[4] == board[7] == marker) or #Left Row
    (board[2] == board[5] == board[8] == marker) or #Middle Row
    (board[3] == board[6] == board[9] == marker) or #Right Row
    (board[1] == board[5] == board[9] == marker) or #LT to RB Diagional
    (board[7] == board[5] == board[3] == marker)) #LB to RT Diagional
    
#Chooses who goes first randomly
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#Space checks if a space had a value
def space_check(board, position):
    return board[position] == ' '

#Checks full board
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

#Players choice of position on board
def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        
        position = input("Pick a position on the board (1-9): ")
        
        if position not in range(1,10) and position.isalpha():
            
            print("Sorry, invalid choice!")
        else:
            position = int(position)

        if space_check(board, position) == False:

            print("Sorry, space is already taken!")
    
    return int(position)

#Do you want to replay?
def replay():
        
    choice = 'Wrong'
    
    while choice not in ['Y','N']:
        
        choice = input("Do you want to play again (Y or N)?: ")
        choice = choice.upper()
        
        if choice not in ['Y','N']:
            print("Sorry, I don't understand, please choose Y or N: ")
    
    if choice == 'Y':
        return True
    else:
        return False


#Setup the game

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' goes first!')
    
    play_game = input('Are you ready to play? Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print(f'Congratulations! {turn} You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print(f'Congratulations! {turn} You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break