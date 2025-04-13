
from graphics import*
#def drawFace(center: tuple, size: int, win: tuple)->tuple:
#draws face different size, how would you do assert?


def main():
    # ipnut the size of the window
    #WIN_WIDTH = 300 #!!! change to input later
    #WIN_HEIGHT = 500 #!!!
    #x,y = eval(input())


    pass

    window_size = (input("size of window?")).split(",")


    size = int(input("size of face (radius)?"))

    center = (input("The center of face?")).split(",")
    print(window_size[0])
    win = GraphWin("Window",(window_size[0]),(window_size[1]))

    circle = Circle(Point((center[0]),(center[1])),size)
    circle.draw(win)
    win.getMouse()

main()












