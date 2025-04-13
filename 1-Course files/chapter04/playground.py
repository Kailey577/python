from graphics import *



g = GraphWin("hi", 500,500)
p = Point(250, 250)
p.draw(g)
c = Circle(p, 10)
c.draw(g)

mouse = g.getMouse()
# make c move to wherever you clicked the mouse!
c.move(-200,-200)



mouse = g.getMouse()
print(mouse)
