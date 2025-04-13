from graphics import *


def loop_stuff():

    # range based
    for i in range(10): print(i)

    # sequences
    # - ordered group of items
    # - iterable


    l = [1,2,3]
    for element in l:
        print(l)

    for t in ('t', 1, (1, 2)):
        print(t)


    for c in "apples":
        print(c)


    file = open('numbers', 'r', encoding='utf-8')

    for line in file:
        print(line)



img = Image(Point(0,0), 'pem1.gif')
width = img.getWidth()
height = img.getHeight()


for row in range(height):
    for col in range(width):
        r,g,b = img.getPixel(col, row)
        avg = sum([r,g,b]) // 3
        new_color = color_rgb(avg,avg,avg)
        img.setPixel(col,row,new_color)
img.save("cat.gif")