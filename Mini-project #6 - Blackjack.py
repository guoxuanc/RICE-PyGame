# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
player = ""
dealer = ""
deck = ""
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        global in_play
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        if in_play and pos == (70, 240):
            card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, (106, 288), CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        message = ""
        for card in self.hand:
            message += (card.get_suit()+card.get_rank()+" ")
        return "Hand contains "+message

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value = 0
        aces = False
        for card in self.hand:
            hand_value += VALUES.get(card.get_rank())
            if card.get_rank() == 'A':
                aces = True
        if not aces:
            return hand_value
        elif hand_value+10 <= 21:
            return hand_value+10
        else:
            return hand_value
   
    def draw(self, canvas, pos):
        offset_x = 1.0
        for card in self.hand:
            card.draw(canvas, ((offset_x*pos[0]), pos[1]))
            offset_x += 0.58
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        message = ""
        for card in self.deck:
            message += (card.get_suit()+card.get_rank()+",")
        return "Deck contains "+message


#define event handlers for buttons
def deal():
    global player, dealer, deck, outcome, in_play, score
    if in_play:
        outcome = "player loses, Hit or Stand?"
        score -= 1
    else:
        outcome = "Hit or Stand?"
    player = Hand()
    dealer = Hand()
    deck = Deck()
    in_play = True
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())

def hit():
    global in_play, player, deck, outcome, score
    # if the hand is in play, hit the player
    if in_play:
        outcome = "Hit or Stand?"
        player.add_card(deck.deal_card())
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "player has busted and lost"
            score -= 1
            in_play = False
    else:
        outcome = "this round is over, you can't hit"
    
       
def stand():
    global in_play, player, dealer, deck, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        outcome = "Hit or Stand?"
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "dealer has busted, player wins"
            score += 1
        elif dealer.get_value() >= player.get_value():
            outcome = "player loses"
            score -= 1
        else:
            outcome = "player wins"
            score += 1
        in_play = False
    else:
        outcome = "this round is over, you can't stand"

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play
    canvas.draw_text("Score: "+str(score), (410, 130), 43, "DarkRed")
    if not in_play:
        canvas.draw_text(": New deal?", (175, 220), 36, "LightBlue")
    canvas.draw_text("Blackjack", (70,100), 82, "Yellow")
    canvas.draw_text("Dealer", (70, 220), 36, "LightBlue")
    canvas.draw_text(outcome, (70, 160), 34, "Black")
    canvas.draw_text("Player", (70, 420), 36, "LightBlue")
    canvas.draw_text(": Your hand value " + str(player.get_value()),
                     (165, 420), 36, "LightBlue")
    dealer.draw(canvas, (70, 240))
    player.draw(canvas, (70, 440))

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# gradic rubric
"""
1 pt - The program displays the title "Blackjack" on the canvas.
1 pt - The program displays 3 buttons ("Deal", "Hit" and "Stand") in the control area.
2 pts - The program graphically displays the player's hand using card images. (1 pt if text is displayed in the console instead)
2 pts - The program graphically displays the dealer's hand using card images. Displaying both of the dealer's cards face up is allowable when evaluating this bullet. (1 pt if text displayed in the console instead)
1 pt - The dealer's hole card is hidden until the current round is over. After the round is over, it is displayed.
2 pts - Pressing the "Deal" button deals out two cards each to the player and dealer. (1 pt per player)
1 pt - Pressing the "Deal" button in the middle of the round causes the player to lose the current round.
1 pt - Pressing the "Hit" button deals another card to the player.
1 pt - Pressing the "Stand" button deals cards to the dealer as necessary.
1 pt - The program correctly recognizes the player busting.
1 pt - The program correctly recognizes the dealer busting.
1 pt - The program correctly computes hand values and declares a winner. Evaluate based on messages.
2 pts - The program accurately prompts the player for an action with messages similar to "Hit or stand?" and "New deal?". (1 pt per message)
1 pt - The program implements a scoring system that correctly reflects wins and losses.
"""
