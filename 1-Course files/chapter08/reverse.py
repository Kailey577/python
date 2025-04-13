from graphics import *

img = Image(Point(0,0),'pem1.gif')

width = int(img.getWidth())
height = int(img.getHeight())
print(width)
print(height)


'''r,g,b = img.getPixel(1,281)
img.setPixel(500,281, color_rgb(r,g,b))

for row in range(height):
    for col in range(width):
        r,g,b = img.getPixel(col, row)
        img.setPixel(width,height,color_rgb(r,g,b))
img.save("cat.gif")'''







first_width = width
x = 1

while height != 1:
    while width != width//2:

        r,g,b = img.getPixel(x,height)
        new_color = color_rgb(r,g,b)
        img.setPixel(width,height, new_color)
        x =+1
        width =-1
    height =- 1
    width = first_width

'''a = 10
b = 4
full_b = 4

while a != 1:
    while b != b/2:
        print("hello")
        b=b-1
    a = a-1
    b = full_b'''

'''r,g,b = img.getPixel()'''

#so then it would go 2,218

'''for row in range(height):
    for col in range(width):
        r,g,b = img.getPixel(row,col)
        new_color = color_rgb(r,g,b)
        img.setPixel(col,row,new_color)'''
img.save("the_cat.gif")



