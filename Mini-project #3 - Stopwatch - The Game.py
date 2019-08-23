"""
1 pt - The program successfully opens a frame with the stopwatch stopped.
1 pt - The program has a working "Start" button that starts the timer.
1 pt - The program has a working "Stop" button that stops the timer.
1 pt - The program has a working "Reset" button that stops the timer (if running) and resets the timer to 0.
4 pts - The time is formatted according to the description in step 4 above. Award partial credit corresponding to 1 pt per correct digit. For example, a version that just draw tenths of seconds as a whole number should receive 1 pt. A version that draws the time with a correctly placed decimal point (but no leading zeros) only should receive 2 pts. A version that draws minutes, seconds and tenths of seconds but fails to always allocate two digits to seconds should receive 3 pts.
2 pts - The program correctly draws the number of successful stops at a whole second versus the total number of stops. Give one point for each number displayed. If the score is correctly reported as a percentage instead, give only one point.
2 pts - The "Stop" button correctly updates these success/attempts numbers. Give only one point if hitting the "Stop" button changes these numbers when the timer is already stopped.
1 pt - The "Reset" button clears the success/attempts numbers.
"""
import simplegui

# define global variables

# the integer "tracker" is to track of the time in tenths of seconds
# i.e. tracker = 3 means 0.3 second
tracker = 0
# the integer "minute" is to record of the time in minutes
minute = 0
# the string "current_time" records the formatted time
current_time = "0:00.0"
# two numerical counters that keep track of  the total number of stops
# and the number of successful stops at a whole second 
x=0
y=0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    """
    NOTE: 
         Before this function, I've formatted the integer "tracker" in 
    function "time_handler". So in this function I just need to format 
    integer into string. "tracker" always less than 600
    """
    global current_time, minute
    second = 0
    tenths_sec = 0      
    second = tracker%1000/10
    tenths_sec = tracker%10
    
    # allocate two digits to seconds
    if second < 10:
        second = "0"+str(second)
    else:
        second = str(second)
        
    tenths_sec = str(tenths_sec)
    current_time = str(minute)+":"+second+"."+tenths_sec
    return current_time
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global x,y
    if timer.is_running():
        timer.stop()
        y = y+1
        if tracker%10 == 0:
            x += 1
    
def reset():
    global tracker, minute, current_time, x, y
    timer.stop()
    tracker = 0
    minute = 0
    x = y =0
    current_time = "0:00.0"

# define event handler for timer with 0.1 sec interval
def time_handler():
    global tracker, minute
    # The increments of "tracker"
    tracker += 1
    """
    The "tracker" means the time in tenths of seconds
    i.e.,599 represents 59.9 seconds
    When the tracker increases to 600. It means we have 1 minute.
    So we have to reset the tracker to 0 & add 1 into "minute"
    And if the "minute" reach to 60, we have to reset the "minute" to 0
    """
    if tracker == 600:
        tracker = 0
        minute += 1
        if minute == 60:
            minute = 0
            

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(), [100, 115], 55, "White")
    canvas.draw_text(str(x)+"/"+str(y),[290,30],25,"Green")
    
# create frame & timer
frame = simplegui.create_frame("Stopwatch",350,200)
timer = simplegui.create_timer(100, time_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame 
frame.start()

# Please remember to review the grading rubric
