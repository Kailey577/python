from graphics import*

win = GraphWin("car",500,500)

c=Line(Point(50,170), Point(220,100))
c.draw(win)
c=Line(Point(220,100), Point(470,140))
c.draw(win)
c=Line(Point(470,140), Point(50,170))#end point
c.draw(win)
c=Line(Point(470,140), Point(465,190))#back end
c.draw(win)
c=Line(Point(465,190), Point(430,195))
c.draw(win)
c=Line(Point(430,195), Point(400,170))
c.draw(win)
c=Line(Point(400,170), Point(359,173))
c.draw(win)
c=Line(Point(359,173), Point(338,205))
c.draw(win)
c=Line(Point(338,205), Point(130,212))
c.draw(win)
c=Line(Point(130,212), Point(110,185))
c.draw(win)
c=Line(Point(110,185), Point(72,187))
c.draw(win)
c=Line(Point(72,187), Point(45,212))
c.draw(win)
c=Line(Point(45,212), Point(50,170))
c.draw(win)
c=Line(Point(45, 212), Point(45,235))
c.draw(win)

c=Line(Point(45, 235), Point(30,230))
c.draw(win)
c=Line(Point(30, 230), Point(28,213))
c.draw(win)
c=Line(Point(28, 213), Point(45,212))
c.draw(win)
c=Line(Point(31, 213), Point(31,210))
c.draw(win)
c=Line(Point(31, 210), Point(31,176))
c.draw(win)
c=Line(Point(31, 176), Point(50,170))
c.draw(win)
c=Line(Point(31, 182), Point(50,179))
c.draw(win)

ROUND=Circle(Point(88,230), 35.5)
ROUND.draw(win)
ROUND=Circle(Point(386,218), 38.5)
ROUND.draw(win)


c=Line(Point(338,205), Point(338,220))
c.draw(win)
c=Line(Point(338,220), Point(130,225))
c.draw(win)
c=Line(Point(130,225), Point(130,212))
c.draw(win)




c=Line(Point(88,162), Point(220,110))
c.draw(win)

c=Line(Point(220,110), Point(320,126))
c.draw(win)

c=Line(Point(320,126), Point(320,140))
c.draw(win)
c=Line(Point(320,140), Point(88,162))
c.draw(win)

win.getMouse()