# -*- coding: utf-8 -*-
"""
1 pt — The game starts immediately when the “Run” button in CodeSkulptor is pressed.

1 pt — A game is always in progress. Finishing one game immediately starts another in the same range.

1 pt — The game reads guess from the input field and correctly prints it out.

3 pts — The game correctly plays “Guess the number” with the range [0, 100) and prints understandable output messages to the console. Play three complete games: 1 pt for each correct game.

2 pts — The game includes two buttons that allow the user to select the range [0, 100) or the range [0, 1000) for the secret number. These buttons correctly change the range and print an appropriate message. (1 pt per button.)

2 pts — The game restricts the player to a finite number of guesses and correctly terminates the game when these guesses are exhausted. Award 1 pt if the number of remaining guesses is printed, but the game does not terminate correctly.

1 pt — The game varies the number of allowed guesses based on the range of the secret number — seven guesses for range [0, 100), ten guesses for range [0, 1000).
"""
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

# input global variables used in your code
remain_guess = 7
num_range = 100
secret_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, num_range)
    global remain_guess
    
    if num_range == 100:
        remain_guess = 7
    else:
        remain_guess = 10
    
    print "New game Range is from 0 to", num_range
    print "Number of remaining guesses is", remain_guess
    print " "


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game   
    global num_range
    num_range = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global remain_guess
    
    guess_number = int(guess)
    remain_guess = remain_guess - 1
    print "Guess was", guess_number
    print "Number of remaining guesses is", remain_guess
    
    if remain_guess >= 0:
        if guess_number == secret_number:
            print "Correct"
            print " "
            new_game()
            
        elif guess_number > secret_number:
            if remain_guess == 0:
                print "Correct number is", secret_number, "Player loses"
                print " "
                new_game()
            else:
                print "Lower"
                print " "
        else:
            if remain_guess == 0:
                print "Correct number is", secret_number, "Player loses"
                print " "
                new_game()
            else:
                print "Higher"
                print " "
    else:
        print "Correct number is", secret_number, "Player loses"
        print " "
        new_game()

# create frame
f = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
