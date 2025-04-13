import math
from random import random

from graphics import *

# Challenge: can you make the drawing wrap around to the other side
# hint modulos(remainder)
#is percent sign for remainder
print(2355555 % 7 )
def main():
    win = GraphWin("Random Walk", 500,500)
    win.setCoords(0,0,100,100) #0,00 is bottom left 100,100 is top right

    #start at middle
    y = 50
    x = 90
    for _ in range(10000):
        angle = random() * 2 * math.pi
        scale = 0.05
        new_x = (x + math.cos(angle) + scale) % 100
        new_y = ((y + math.sin(angle)) + scale) % 100

        # connect the dots
        #line = Line(Point(x,y), Point(new_x, new_y))
        #line.draw(win)
        p = Point(new_x, new_y)
        p.draw(win)
        # update your current position
        x,y = new_x, new_y
    #wait for user to close
    win.getMouse()
    win.close()




main()