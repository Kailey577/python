from graphics import *

img = Image(Point(0,0), 'pem1.gif')
width = img.getWidth()
height = img.getHeight()

for row in range(height):
    for col in range(width):
        r,g,b = img.getPixel(col, row)
        r = min(r+40,225)
        b = min(b+25,225)
        g = min(g+10,225)
        new_color = color_rgb(r,g,b)
        img.setPixel(col,row,new_color)
img.save("rose_cat.gif")