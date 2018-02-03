#----------------------------------------------
# Author: Alex Tseng
# For: CSCI107, Rance Harmon
# Last Updated: February 2, 2018
#----------------------------------------------
# This script will attempt to make a character
# from Thomas the Tank Engine using Turtle
# graphics from python. 
# Note: This creates the character starting
# 	from the background to the 
#	foreground.
#----------------------------------------------

import turtle 	#imports turtle graphics for use
wn = turtle.Screen() 	#creates new window entitled thomas
thomas = turtle.Turtle()
thomas.penup()

# Background of thomas
thomas.goto(-30,-30)
thomas.pendown()
thomas.fillcolor("aqua")
thomas.begin_fill()
for i in range(0,2):
	thomas.forward(60)
	thomas.left(90)
	thomas.forward(90)
	thomas.left(90)
thomas.end_fill()
thomas.penup()

# Background 2 of thomas
thomas.goto(-40,0)
thomas.pendown()
thomas.fillcolor("aqua")
thomas.begin_fill()
for i in range (0,2):
	thomas.forward(80)
	thomas.left(90)
	thomas.forward(30)
	thomas.left(90)
thomas.end_fill()
thomas.penup()

# Bottom rail thing
thomas.goto(-50,-40)
thomas.pendown()
thomas.fillcolor("lightgrey")
thomas.begin_fill()
for i in range (0,2)
	thomas.forward(100)
	thomas.left(90)
	thomas.forward(10)
	thomas.left(90)
thomas.end_fill()
thomas.penup()

# Even more bottom rail thing
thomas.goto(-60,-60)
thomas.pendown()
thomas.fillcolor("red")
thomas.begin_fill()
for i in range (0,2)
	thomas.foward(120)
	thomas.left(90)
	thomas.forward(20)
	thomas.left(90)
