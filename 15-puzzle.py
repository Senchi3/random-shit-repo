# TODO: Make work on Mac and Linux

from msvcrt import getch
import sys
import os
from os import system, name
import random


board = """"""
solved_board = """
    01 02 03 04
    05 06 07 08
    09 10 11 12
    13 14 15 []
    """
empty_piece_pos = 0
count = 0


# Clear console
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Crash in case smth bad happens
def crash():
    clear()
    print("Oops! You pressed a key that doesn't work. Remember to only use the arrow keys!\n Press any key to continue.")
    getch()
    os.execv(sys.argv[0], sys.argv)


# Piece movement function
def move(key):
    if key == 72:  # Up arrow
        move('u')
    elif key == 75:  # Left arrow
        move('l')
    elif key == 77:  # Right arrow
        move('r')
    elif key == 80:  # Down arrow
        move('d')
    else:
        crash()


# Randomly generate a game board
# TODO: This function currently can create duplicate numbers, and replacing 0 with [] does not work.

def generate_board():
    numbers = random.sample(range(16), 16)
    new_numbers = []
    for number in numbers:
        if number == 0:
            new_numbers.append("[]")
        elif number < 10:
            new_numbers.append("0{}".format(str(number)))
        else:
            new_numbers.append(str(number))
    return """
    {} {} {} {}
    {} {} {} {}
    {} {} {} {}
    {} {} {} {}
    """.format(new_numbers[0], new_numbers[1], new_numbers[2], new_numbers[3], 
               new_numbers[0], new_numbers[5], new_numbers[6], new_numbers[7], 
               new_numbers[0], new_numbers[9], new_numbers[10], new_numbers[11], 
               new_numbers[12], new_numbers[13], new_numbers[14], new_numbers[15])



# Game loop
while True:
    
    if count == 0:
        board = generate_board()
    count =+ 1
    clear()

    # Find current empty piece and make its index the variable. The amount of characters on the board is always the same, so the indexes will always be:
    # 4  7  10 13
    # 20 23 26 29
    # 36 39 42 45
    # 52 55 58 61

    empty_piece_pos = board.find('[]')

    # THIS IS WHAT DISPLAYS ON THE CONSOLE

    print ("Turn #{}".format(count))
    print(board)
    if board == solved_board:
        print("Congratulations, you won! Press Escape to close the game.")
    else:
        print ("Press an arrow key to make your next move, or Escape to close the game.")

    # Get keys

    key = ord(getch())
    if key == 27:  # ESC
        break
    elif key == 224:  # Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        move(key)