

from graphics import*

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50),Point(150,150))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range (10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX()-c.getX()
        dy = p.getY()-c.getY()
        shape = Rectangle(Point(dx,dy),Point(dx+100,dy+100))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)





    win.close()
main()