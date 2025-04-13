from graphics import*

win = GraphWin("Line Segment", 200, 200)

p1 = win.getMouse()
p1.draw(win)

p2 = win.getMouse()
p2.draw(win)

dx = x2 - x1
dy = y2 - y1
segment = Line(Point(p1),Point(p2))

segment.draw(win)

