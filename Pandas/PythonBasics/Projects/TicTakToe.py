#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 22:45:24 2020

@author: rohyth
"""

'------GLOBAL Variables-----------------'
game_still_going = True
winner = None
current_player = 'X'


'Game Board'
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]




def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print(board[6] + " | " + board[7] + " | " + board[8] )
    

def play_game():
    display_board()
    
    while game_still_going:
    
        handle_turn(current_player)
        
        check_if_game_over()
        
        # flip to the other player
        flip_player()
        
    if winner == 'X' or winner == 'O':
        print('The Winner of the Game is : ' , winner)
    elif winner == None :
        print('Tie Match')
    
    
    
def handle_turn(player):
    
    print()
    print(player + "'s turn.")
    
    position = input('Choose a position from 1-9: ')
    
    valid = False
    while not valid:
        
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input('Choose a position from 1-9: ')
                 
            
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print('Space Already filled. Try Again')
            
            
    board[position] = player    
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()
    

def check_for_winner():
    # check rows
    # check columns
    # check columns
    
    global winner
    
    row_winner = check_row()    
    column_winner = check_column()
    diagnal_winner = check_diagnal()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner == None
    
    return



def check_row():
    # Set global variables    
    global game_still_going
    
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    
    if row1 or row2 or row3:
        game_still_going = False
    
    # return the winne X or O
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    
    return

def check_column():
    
    global game_still_going
    
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    
    if col1 or col2 or col3:
        game_still_going = False
    
    # return the winne X or O
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    
    return

def check_diagnal():
    
    global game_still_going
    
    dig1 = board[0] == board[4] == board[8] != "-"
    dig2 = board[2] == board[4] == board[6] != "-"
    
    if dig1 or dig2:
        game_still_going = False
    
    # return the winne X or O
    if dig1:
        return board[0]
    elif dig2:
        return board[2]
    
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return




def flip_player():
    global current_player
    
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return



play_game()