from graphics import*

def main():
    win = GraphWin("Face", 100,100)

    Round = Circle(Point(50,50),50)
    Round.draw(win)


    win.getMouse()

main()