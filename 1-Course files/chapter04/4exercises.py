'''1. Using graphics . py allows graphics to be drawn in a Python shell window.
true
2.  Traditionally, the upper-left comer of a graphics window has coordinates
(0,0).
true
3. A single point on a graphics screen is called a pixel.
true

6. The statement myShape . move ( 10 , 20) moves myShape to the point (10,20).
true

MULTIPLE CHOICE

1. A method that returns the value of an object's instance variable is called a(n)
(d)accessor
2. A method that changes the state of an object is called a(n)
(b) mutator
3. What graphics class would be best for drawing a square?
d) rectangle
4.
What command would set the coordinates of win to go from (0,0) in the lower-left corner to (10,10) in the upper-right?
c.win.setcoords(O, 0, 10, 10)
5. What expression would create a line from (2,3) to (4,5)?
d) Line(Point(2,3) , Point(4,5))
6.What command would be used to draw the graphics object shape into the graphics window win?
d) shape . draw (win)
7. Which of the following computes the horizontal distance between points p1 and p2?
d)abs(p1.getX() - p2.getX())
10. 10. What color is color_rgb (0 , 255 , 255) ?
b) cyan
DISCUSSION
1. Pick an example of an interesting real-world object
and describe it as a programming object by listing its data
(attributes, what it "knows") and its methods (behaviors, what it can "do").

-Cat- (attributes)name is Ember, 4 years old, adopted at 4 months
        (behaviors)sleep, play, meow

2.

a) Point(130,130)
-creates point at coordinate
b) c = Circle(Point(30,40),25)
 c . setFill ( "blue " )
c . setOutline ( "red" )
-creates blue circle with red outline at coordinates with radius
c)creates a red square with a thicker outline
d)creates a line with arrow that goes up (red)
e)creates an oval
f)creates orange hour glass
g)creates text "hello world" changes size and font

3. Describe what happens when the following interactive graphics program runs:
-draws a red circle, (10 times - center, subtract coordinates, move(circle moves where mouse clicks)

'''

from graphics import*

win = GraphWin("car",500,500)
win.setCoords(0, 0, 10, 10)
c=Line(Point(1,1), Point(8,8))
c.draw(win)
d=abs(Point(1,1).getX() - Point(2,2).getX())
print(d)
win.getMouse()
