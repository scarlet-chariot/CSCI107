# -----------------------------------------+
# your name, your partner's name           |
# CSCI 107, Assignment 9                   |
# Last Updated: ??                         |
# -----------------------------------------|
# Draw recursive squares.                  |
# -----------------------------------------+

import turtle
import random

square = turtle.Turtle()
square.hideturtle()
square.speed(0)

window = turtle.Screen()
window.colormode(255)

def draw_squares(variable1,variable2,variable3,variable4,variable5):
	if variable5 == 1:
		r= random.randint(0,255)
		g= random.randint(0,255)
		b= random.randint(0,255)
		variable1.penup()
		variable1.goto(variable2,variable2)
		variable1.fillcolor(r,g,b)
		variable1.begin_fill()
		variable1.pendown()
		for i in range(4):
			square.fd(variable4)
			square.lt(90)
	else:
		


print("Recursive Squares Program")
print("-------------------------")
level = int(input("Enter the level of recursion from 1 to 7: "))
side_length = int(input("Enter the length of a side from 200 to 600: "))

draw_squares(square, -side_length/2, side_length/2, side_length, level)

window.exitonclick()
