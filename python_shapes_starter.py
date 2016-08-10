'''
Some turtle functions you can use to make your shapes


forward(<distance>) - This function takes a positive or negative number and
will move the turtle forward.

back(<distance>) - This function takes a positive or negative numbers and
it will move the turtle back.

right(<angle>) - This function takes a number that represents
angle in degrees. It will turn the turtle to  its right

left(<angle>) - This functions takes an number that represents
 an angle in degrees. It will turn the turtle to its left.

pencolor(<color>) - This functions takes a string that represents a color. The
turtle's pen will draw in that color. The possible color values can be found
at https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

penup() - This function takes no parameters. When called it will
lift the turtle's pen up, the turtle will not draw when moved.

pendown() - This function takes no parameters. When called it will put the
turtle's pen down. It will draw when moved.

speed(<number>) - This function takes a number. It determines how fast the
turtle moves around the screen. Strangely enough if you want it to go as
fast as possible you have to pass it 0 as a parameter.

goto(<x>, <y>) - This function takes two numbers, a position along the x-axis
and a position along the y-axis. It will move the turtle to that position.

fillcolor(<color>) - This function takes a string that represents a color. The
color will be used to fill shape the turtle has made. In order to get the turtle
to fill the shape you have to use the begin_fill() function before the turtle
starts drawing the shape and the end_fill() function after it finishes for the
shape to be filled in.

begin_fill() - This function takes no parameters. It is put before the turtle
draws a shape that you want filled in.

end_fill() - This function takes no parameters. It is put after the turtle has
finished drawing a shape that you want filled in.

dot(<size>, <color>) - This function takes two parameters. The first is a
positive number that represents the diameter of the dot to be drawn by the
turtle. The second is a string that represents the color the dot should be.


BONUS:

circle(<radius>, <extent>, <steps>) - This function takes three parameters.
However you only have to put in the first one. The <radius> parameter is the
necessary parameter, it is a number that represents the radius of the circle.
The <extent> is optional. It represents an angle saying how much of the circle
should be drawn, if you don't put in anything for <extent> it will draw the whole
circle. If you put in 180, it will draw a half circle. The third parameter
<steps> is a number that represents how many steps the turtle should take to
draw the circle. Try setting <steps> as 5 to see what happens.


'''



from turtle import *

# START WRITING YOUR CODE HERE

def irregular_polygon(length,width,color):
	penup()
	goto(-350,-100)
	pencolor(color)
	pendown()
	fillcolor(color)
	speed(5)
	begin_fill()
	for i in range(2):
		forward(length)
		left(90)
		forward(width)
		left(90)
	end_fill()
	penup()
irregular_polygon(550,200,'green')

def regular_polygon(number_of_sides,steps,color): 
	side_angle = 360 / number_of_sides
	penup()
	goto(-300,0)
	pencolor(color)
	pendown()
	fillcolor(color)
	speed(5)
	for i in range(5):
		pendown()
		begin_fill()
		for i in range(number_of_sides):
			forward(steps)
			left(side_angle)
		end_fill()
		penup()
		forward(100)
regular_polygon(3,50,'firebrick')

def regular_polygon2(number_of_sides,steps,color): 
	side_angle = 360 / number_of_sides
	penup()
	goto(-300,-50)
	pencolor(color)
	pendown()
	fillcolor(color)
	speed(5)
	for i in range(5):
		pendown()
		begin_fill()
		for i in range(number_of_sides):
			forward(steps)
			left(side_angle)
		end_fill()
		penup()
		forward(100)
regular_polygon2(4,50,'blue')

def irregular_polygon2(length,width,color):
	penup()
	goto(-270,-50)
	pencolor(color)
	fillcolor(color)
	speed(5)
	for i in range(5):
		pendown()
		begin_fill()
		for i in range(2):
			forward(length)
			left(90)
			forward(width)
			left(90)
		end_fill()
		penup()
		forward((100))
irregular_polygon2(10,30,'purple')

def window(number_of_sides2,steps2,color2):
	penup()
	goto(-290,-20)
	pencolor(color2)
	pendown()
	speed(5)
	for i in range(5):
		pendown()
		for i in range(number_of_sides2):
			forward(steps2)
			left(90)
		penup()
		forward(100)
window(4,10,'orange')

def sun(size,color3):
	penup()
	goto(-230,200)
	speed(1)
	pendown()
	dot(size,color3)
	penup()
sun(100,'yellow')

def bird(color4):
	penup()
	goto(200,200)
	speed(1)
	pencolor(color4)
	left(90)
	pendown()
	for i in range(2):
		circle(10,180,20)
		left(180)
		forward(1)
	penup()
bird('blue')