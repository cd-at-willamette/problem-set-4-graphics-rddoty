############################################################
# Name: Reagan
# Name(s) of anyone worked with: Jace higa
# Est time spent (hr): 1 hour
############################################################

from pgl import GWindow, GOval, GRect, GLine, GLabel

GWINDOW_WIDTH = 700
GWINDOW_HEIGHT = 280

def draw_image():
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    red = GRect(0, 0, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    red.set_color("Red")
    red.set_filled(True)
    gw.add(red)
    orange = GRect(0, 40, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    orange.set_color("Orange")
    orange.set_filled(True)
    gw.add(orange)
    white = GRect(0, 120, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    white.set_color("White")
    white.set_filled(True)
    gw.add(white)
    pink = GRect(0, 160, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    pink.set_color("Pink")
    pink.set_filled(True)
    gw.add(pink)
    magenta = GRect(0, 240, GWINDOW_WIDTH, GWINDOW_HEIGHT)
    magenta.set_color("Magenta")
    magenta.set_filled(True)
    gw.add(magenta)
    circle = GOval(310, 140, 100, 40)
    circle.set_color("Black")
    circle.set_filled(True)
    gw.add(circle)
    line = GLine(330, 170, 390, 170)
    line.set_color("White")
    gw.add(line)
    label = GLabel("go lesbians!", 320, 170 )
    label.set_color("White")
    gw.add(label)



if __name__ == '__main__':
    draw_image()
