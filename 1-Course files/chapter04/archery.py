from graphics import*
CX = 150 #center of target
CY = 150
WIN_WIDTH = 300
WIN_HEIGHT = 300
YELLOW_RADIUS = WIN_WIDTH/5#60
RED_RADIUS = WIN_WIDTH/6.25#48
BLUE_RADIUS = WIN_WIDTH/8.33#36
BLACK_RADIUS = WIN_WIDTH/12.5#radius is 24#width is 48
WHITE_RADIUS = WIN_WIDTH/25#radius is 12#width is 24


win = GraphWin("archery",300,300)

A=Circle(Point(CX,CY), YELLOW_RADIUS)
A.setFill("yellow")
A.draw(win)


B=Circle(Point(CX,CY),RED_RADIUS)
B.setFill("red")
B.draw(win)


c=Circle(Point(CX,CY),BLUE_RADIUS)
c.setFill("blue")
c.draw(win)


d=Circle(Point(CX,CY),BLACK_RADIUS)
d.setFill("black")
d.draw(win)

e=Circle(Point(CX,CY),WHITE_RADIUS)
e.setFill("white")
e.draw(win)
win.getMouse()