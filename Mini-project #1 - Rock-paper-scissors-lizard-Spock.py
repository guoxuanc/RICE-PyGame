"""
2 pts — A valid CodeSkulptor URL was submitted. Give no credit if solution code was pasted into the submission field. Give 1 pt if an invalid CodeSkulptor URL was submitted.
2 pts — Program implements the function rpsls() and the helper function name_to_number() with plausible code. Give partial credit of 1 pt if only the function rpsls() has plausible code.
1 pt — Running program does not throw an error.
1 pt — Program prints blank lines between games.
2 pts — Program prints "Player chooses player_choice" where player_choice is a string of the form "rock", "paper", "scissors", "lizard" or "Spock". An example of a complete line of output is "Player chooses scissors". Give 1 pt if program prints out number instead of string.
2 pts — Program prints "Computer chooses comp_choice" where comp_choice is a string of the form "rock", "paper", "scissors", "lizard" or "Spock". An example of a complete line of output is "Computer chooses scissors". Give 1 pt if program prints out number instead of string.
1 pt — Computer's guesses vary between five calls to rpsls() in each run of the program.
1 pt — Computer's guesses vary between runs of the program.
3 pts — Program prints either "Player and computer tie!", "Player wins!" or "Computer wins!" to report outcome. (1 pt for each message.)
3 pts — Program chooses correct winner according to RPSLS rules. Please manually examine 5 cases for correctness. If all five cases are correct, award 3 pts; four cases correct award 2 pts; one to three cases correct award 1 pt; no cases correct award 0 pts.
"""

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
     # convert name to number
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "error"

def number_to_name(number):
    # convert number to a name
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print "error"
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print 
    
    # print out the message for the player's choice
    print 'Player chooses', player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_num = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    computer_num = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    # print out the message for computer's choice
    print 'Computer chooses', number_to_name(computer_num)
    
    # compute difference of comp_number and player_number modulo five
    result = (computer_num - player_num ) % 5
    # use if/elif/else to determine winner, print winner message
    if result<3 and result>0:
        print 'Computer wins!'
    elif result>=3:
        print 'Player wins!'
    else:
        print 'Player and computer tie!'
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")



