########################################
# Name: Reagan
# Collaborators: jimmy
# Estimated time spent (hrs): 1.5 hour
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

from pgl import GWindow, GRect

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
BRICK_WIDTH = 30
BRICK_HEIGHT = 14
BRICKS_IN_BASE = 15

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
def draw_pyramid(BRICKS_IN_BASE):
    if BRICKS_IN_BASE < 0:     
        return
    for i in range(BRICKS_IN_BASE):
        brick_center_x = GWINDOW_WIDTH/2 - ((BRICK_WIDTH/2)*i+1)
        brick_center_y = GWINDOW_HEIGHT - (BRICKS_IN_BASE*BRICK_HEIGHT-(BRICK_HEIGHT*i))
        brick = GRect(brick_center_x, brick_center_y, BRICK_WIDTH, BRICK_HEIGHT)
        brick.set_color('Black')
        brick.set_filled(False)
        gw.add(brick)
        row_brick = GRect(brick.get_x()+BRICK_WIDTH*i, brick.get_y(), BRICK_WIDTH, BRICK_HEIGHT)
        row_brick.set_color('Black')
        row_brick.set_filled(False)
        gw.add(row_brick)
    draw_pyramid(BRICKS_IN_BASE-2)







# Startup code

if __name__ == "__main__":
    draw_pyramid(BRICKS_IN_BASE)

















