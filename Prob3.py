########################################
# Name: Reagan Doty
# Collaborators: Whitley Step, Jace Higa, Jimmy
# Estimate time spent (hrs): 2
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    square = GRect(225,225,SQUARE_SIZE,SQUARE_SIZE)
    square.set_filled(True) #Square Initial Placement
    square.set_color("pink")
    gw.add(square)
    
    score = 0
    score_tally = GLabel(str(score), 40 , 460) #Score Label
    score_tally.set_font(SCORE_FONT)    
    gw.add(score_tally) 
    
    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(e):
        nonlocal score
        square_x = square.get_x() #Gets current x and y coordiante of square
        square_y = square.get_y()
        mouse_x = e.get_x() #Gets mouse x and y coordinate
        mouse_y = e.get_y()
        object_x = random.randint(0, GW_WIDTH - SQUARE_SIZE) # Gives a random x and y coordinate to new square
        object_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)         
        if ((mouse_x <= (square_x + (SQUARE_SIZE))) and (mouse_x >= (square_x))) and ((mouse_y <= (square_y + (SQUARE_SIZE))) and (mouse_y >= (square_y))): #If the mouse clicks on square then it moves square and adds to score
            print("good")
            gw.remove(square)
            gw.add(square, object_x, object_y)
            score = score + 1
            score_tally.set_label(str(score))
            gw.add(score_tally)
        else:         #if they don't click on the square the score goes back to zero
            print("fail")
            score = 0
            score_tally.set_label(str(score))
            
    gw.add_event_listener('click', on_mouse_down)

if __name__ == '__main__':
    clicky_box()
