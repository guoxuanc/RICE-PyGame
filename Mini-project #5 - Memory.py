"""
1 pt - The game correctly draws 16 cards on the canvas (horizontally or as a grid). Using images in place of textual numbers is fine. However, it is the submitter's responsibility to ensure that custom images load during peer assessment.
1 pt - The cards appear in eight unique pairs.
1 pt - The game ignores clicks on exposed cards.
1 pt - At the start of the game, a click on a card exposes the card that was clicked on.
1 pt - If one unpaired card is exposed, a click on a second unexposed card exposes the card that was clicked on.
1 pt - If two unpaired cards are exposed, a click on an unexposed card exposes the card that was clicked on and flips the two unpaired cards over.
1 pt - If all exposed cards are paired, a click on an unexposed card exposes the card that was clicked on and does not flip any other cards.
1 pt - Cards paired by two clicks in the same turn remain exposed until the start of the next game.
1 pt - The game correctly updates and displays the number of turns in the current game in a label displayed in the control area. The counter may be incremented after either the first or second card is flipped during a turn.
1 pt - The game includes a "Reset" button that resets the turn counter and restarts the game.
1 pt - The deck is also randomly shuffled each time the "Reset" button is pressed, so that the cards are in a different order each game.
"""

# implementation of card game - Memory

import simplegui
import random


card_deck = range(8) + range(8)
exposed = []
state = 0
last = 100
turn = 0


# helper function to initialize globals
def new_game():
    global card_deck, exposed, state, turn
    
    turn = 0
    label.set_text("Turn = " + str(turn))
    state = 0
    exposed = []
    # shuffle the cards to random order
    random.shuffle(card_deck)  
    
    # Set exposed variable to list of list 
    # [0 Visible, 1 Center, 2 Matched, 3 Card Value] 
    center = 25
    for itr in range(1, 17):
        exposed += [[False, center, False, card_deck[itr-1], "White"]]
        center += 50 
        
# helper function to get index     
def check_card(p):
    global exposed 
    
    # returns the index of by the list in list exposed
    for index, exp in enumerate(exposed):
        if exp[1] + 25 >= p[0] >= exp[1] - 25:
            return int(index)
        
# tracks the counters and label
def counter_help():
    global state, turn
    
    state = 1
    turn += 1
    label.set_text("Turn = " + str(turn))
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, last
    
    click_pos = list(pos)
    
    # when no cards are flipped
    if state == 0:
        exposed[check_card(click_pos)][0] = True
        counter_help()
        last = check_card(click_pos)
    # when 1 card is flipped
    elif state == 1:
        if exposed[check_card(click_pos)][0] == False:
            exposed[check_card(click_pos)][0] = True
            state = 2
            # found a match
            if exposed[last][3] == exposed[check_card(click_pos)][3]:
                exposed[last][2] = True
                exposed[last][4] = "Gray"
                exposed[check_card(click_pos)][2] = True
                exposed[check_card(click_pos)][4] = "Gray"
    # when 2 cards are flipped, clicking on new card
    else:
        for exp1 in exposed:
            # check if matched in memory, if not then flip over
            if exp1[2] == False:
                exp1[0] = False
            
        # flip the new card
        exposed[check_card(click_pos)][0] = True
        counter_help()
        last = check_card(click_pos)
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    
    # Draws the numbers in card_deck
    xaxis = 0
    for card in exposed:
        canvas.draw_text(str(card[3]), (8 + xaxis, 75), 70, card[4])
        xaxis += 50
    
    # Draw the box to hide cards
    for expo in exposed:
        if expo[0] == False:
            canvas.draw_line((expo[1], 0), (expo[1], 100), 50, "LightBlue") 
    
    # Cosmetic line
    for lne in range(1,17):
        canvas.draw_line((lne * 50, 0), (lne * 50, 100), 1, "White")
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric

