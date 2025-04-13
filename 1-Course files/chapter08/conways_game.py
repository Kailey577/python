#RULES:
'''ANY CELLS WITH FEWER THAN TWO NEIGHBORS DIE, CELLS WITH TWO TO THREE NIEGHBORS LIVE ON TO NEXT GENERATION,
 ANY CELL WITH MORE THAN THREE NEIGHBORS DIE,ANY DEAD CELLS WITH EXACTLY THREE NEIGHBORS BECOME LIVE CELL'''






from graphics import*


def main():
    graph = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    def spawn(placement_row: int, placement_in_row: int):
        "creates a grid, 1 equals a cell, 0 equals no cells, allows to place cell."
        graph[placement_row][placement_in_row]=1
        print(graph)



    def create_graph():
        win = GraphWin("The grid",300,300)
        win.setCoords(0,0,3,3)
        #horizontal lines of the grid
        a_line = Line(Point(0,1), Point(3,   1))
        a_line.draw(win)
        a_line = Line(Point(0, 2), Point(3, 2))
        a_line.draw(win)
        #vertical lines of the grid
        a_line = Line(Point(1, 0), Point(1, 3))
        a_line.draw(win)
        a_line = Line(Point(2, 0), Point(2, 3))
        a_line.draw(win)

        #generating the cells
        click_count = 0

        while click_count<9:
            click = win.getMouse()
            row, col = int(click.getY()), int(click.getX())
            if click:
                a_cell = Circle(click,0.2)
                a_cell.draw(win)
                click_count += 1
                are_you_done = input("Are you done clicking?")
                if are_you_done == "yes":
                    break


        win.getMouse()

    def on_tic():
        user_input = input("Next generation?")
        if user_input == "yes":

        if user_input == "no":






     spawn(0,0)
    spawn(0,1)
    spawn(0,2)
    create_graph()
    def checking_neighbors():
        "determines if cells live or die"
        if sum(graph) == 1:
            #die
        if sum(graph) == 2:
            #die
        if sum(graph) == 3:
            #die



    #QUESTIONS:
    #How to make it so that you can't place multiple cells in one box of grid?
    #If right next to each other

main()