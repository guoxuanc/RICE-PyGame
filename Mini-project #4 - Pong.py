"""
1 pt - The ball spawns in the middle of the canvas with either an upward left or an upward right velocity. No credit if the ball moves only horizontally left or right. Bleh, that would be boring!
2 pts - The ball bounces off of the top and bottom walls correctly. (1 pt each)
2 pts - The ball respawns in the middle of the screen when it strikes the left or right gutter but not the paddles. (1 pt for each side) Give credit for this item even if the ball hits the edge of the canvas instead of the gutter.
1 pt - The left and right gutters (instead of the edges of the canvas) are properly used as the edges of the table.
1 pt - The ball spawns moving towards the player that won the last point.
2 pts - The 'w' and 's' keys correctly control the velocity of the left paddle as described above. Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to 'w' and 's' key presses.)
2 pts - The up and down arrows keys correctly control the velocity of the right paddle as described above. Please test each key in isolation. (1 pt if the paddle moves, but in an incorrect manner in response to up and down arrow key presses.)
2 pts - The edge of each paddle is flush with the gutter. (1 pt per paddle)
2 pts - The paddles stay on the canvas at all times. (1 pt per paddle)
2 pts - The ball correctly bounces off the left and right paddles. (1 pt per paddle)
1 pt - The scoring text is positioned and updated appropriately. The positioning need only approximate that in the video.
1 pt - The game includes a "Restart" button that resets the score and relaunches the ball.

"""
# Implementation of classic arcade game Pong

import simplegui
import random
import math 

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

ball_pos = [WIDTH / 2, HEIGHT / 2 ]
ball_vel = [0,  0]

paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2 ]
    if direction == LEFT:
        #the velocity of ball with an upward left direction
        ball_vel[0] = random.randrange(120 / 60, 240 / 60) * (-1)
        ball_vel[1] = random.randrange(60 / 60, 180 / 60) * (-1)
        
    else:
        #the velocity of ball with an upward right direction
        ball_vel[0] = random.randrange(120 / 60, 240 / 60) 
        ball_vel[1] = random.randrange(60 / 60, 180 / 60) * (-1)
        


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    
    #the ball collides with and bounces off of the top and bottom walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    #If the ball touches the left or right gutter
    if ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH:
        if ball_pos[1] >= paddle2_pos - PAD_HEIGHT/2 and ball_pos[1] <= paddle2_pos + PAD_HEIGHT/2:
            #the bal strikes the right paddle, bounces off
            ball_vel[0] *= -1
            #increase the velocity of the ball by 10%
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            #the bal fails to strike the right paddle,respawn the ball
            #in the center of the table headed towards the opposite gutter
            spawn_ball(LEFT)
            #the left player receives a point
            score1 += 1
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos - PAD_HEIGHT/2 and ball_pos[1] <= paddle1_pos + PAD_HEIGHT/2:
            #the bal strikes the left paddle, bounces off
            ball_vel[0] *= -1
            #increase the velocity of the ball by 10%
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            #the bal fails to strike the left paddle,respawn the ball
            #in the center of the table headed towards the opposite gutter
            spawn_ball(RIGHT)  
            #the right player receives a point
            score2 += 1 
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    check1 = paddle1_pos + paddle1_vel
    if check1 >= PAD_HEIGHT/2 and check1 <= HEIGHT - PAD_HEIGHT/2:
        paddle1_pos += paddle1_vel
        
    check2 = paddle2_pos + paddle2_vel
    if check2 >= PAD_HEIGHT/2 and check2 <= HEIGHT - PAD_HEIGHT/2:
        paddle2_pos += paddle2_vel
        
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos-40],[0,paddle1_pos+40],[PAD_WIDTH,paddle1_pos+40],[PAD_WIDTH,paddle1_pos-40]], 1, "White", "White")
    canvas.draw_polygon([[WIDTH-PAD_WIDTH-1,paddle2_pos-40],[WIDTH-PAD_WIDTH-1,paddle2_pos+40],[WIDTH-1,paddle2_pos+40],[WIDTH-1,paddle2_pos-40]], 1, "White", "White")    
    
    # draw scores
    canvas.draw_text(str(score1), [150,60], 60, "White")
    canvas.draw_text(str(score2), [450,60], 60, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= 4
        
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel += 4    
        
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 4
        
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 4      
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += 4
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel -= 4   
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += 4
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel -= 4  


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_label('Press the "Reastart" bottom to start a new game')
frame.add_label(" ", 80)
frame.add_button("Restart", new_game, 180)

# start frame
#new_game()
frame.start()
