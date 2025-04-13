
from graphics import *
def main():
    win = GraphWin("House",300,300)
    win.setCoords(2,2,8,8)

    h1 = win.getMouse()
    #h1.draw(win)
    h2 = win.getMouse()
    #h2.draw(win)

    rectangle = Rectangle(h1,h2)
    rectangle.draw(win)
#----- Door
    width = (rectangle.getWidth())/5

    print(width)
    #door
    half_door_width = width/2
    print(half_door_width)

    door = win.getMouse()


    d1x = door.getX() - half_door_width
    print(d1x)
    d1y = door.getY()

    d2x = door.getX() + half_door_width
    print(d2x)
    d2y = h2.getY()

    #rectangle_door = Rectangle((d1x,d1y),(d2x,d2y))
    #rectangle_door.draw(win)

    #.....roof
    roof = win.getMouse()
    r1x = roof.getX()
    r1y = roof.getY()

    r2x = h1.getX()
    r2y = h1.getY()

    r3x = h2.getX()
    r3y = h1.getY()

    triangle = Polygon((r1x,r1y),(r2x,r2y),(r3x,r3y))
    triangle.draw(win)



#window

    window = win.getMouse
   # square = Rectangle

  #  square.draw(win)





main()

