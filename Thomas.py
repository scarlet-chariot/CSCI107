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
thomas.speed(0) 		#Sets turtle speed to fastest (0)
thomas.penup()

# Background of thomas
thomas.goto(-30,-30)
thomas.pendown()
thomas.fillcolor("aqua")
thomas.begin_fill()
for i in range(0,2):
	thomas.forward(60)
	thomas.left(90)
	thomas.forward(80)
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
for i in range (0,2):
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
for i in range (0,2):
	thomas.forward(120)
	thomas.left(90)
	thomas.forward(20)
	thomas.left(90)
thomas.end_fill()
thomas.penup()

# Left Wheel
thomas.goto(-40,-70)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
for i in range (0,8):
	thomas.forward(5)
	thomas.left(45)
thomas.end_fill()
thomas.penup()

# Right Wheel
thomas.goto(40,-70)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
for i in range (0,8):
	thomas.forward(5)
	thomas.left(45)
thomas.end_fill()
thomas.penup()

# Hat
thomas.goto(-45,50)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
thomas.forward(90)
thomas.left(167.5)
thomas.forward(46.1)
thomas.left(25)
thomas.forward(46.1)
thomas.end_fill()
thomas.penup()

# Pipe
thomas.setheading(0)
thomas.goto(-5,30)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
for i in range(0,2):
	thomas.fd(10)
	thomas.lt(90)
	thomas.fd(40)
	thomas.lt(90)
thomas.end_fill()
thomas.penup()

# Pipe hat
thomas.goto(-8,70)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
for i in range(0,3):
	thomas.fd(16)
	thomas.lt(120)
thomas.end_fill()
thomas.penup()

# Left Dot Freckle thing
thomas.goto(-30,40)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
for i in range(0,8):
	thomas.lt(45)
	thomas.fd(5)
thomas.end_fill()
thomas.penup()

# Right Dot Freckle thing
thomas.setheading(0)
thomas.goto(30,40)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
for i in range(0,8):
	thomas.lt(45)
	thomas.fd(5)
thomas.end_fill()
thomas.penup()

# Left Inner Dot Freckle thing
thomas.setheading(0)
thomas.goto(-30,45)
thomas.pendown()
thomas.fillcolor("yellow")
thomas.begin_fill()
for i in range(0,8):
	thomas.lt(45)
	thomas.fd(5)
thomas.end_fill()
thomas.penup()

# Right Inner Dot Freckle thing
thomas.setheading(0)
thomas.goto(30,45)
thomas.pendown()
thomas.fillcolor("yellow")
thomas.begin_fill()
for i in range(0,8):
	thomas.lt(45)
	thomas.fd(5)
thomas.end_fill()
thomas.penup()

# Face
thomas.setheading(0)
thomas.goto(0,-10)
thomas.pendown()
thomas.fillcolor("lightgrey")
thomas.begin_fill()
for i in range(0,10):
	thomas.fd(15)
	thomas.lt(36)
thomas.end_fill()
thomas.penup()

# Left Sclera
thomas.setheading(0)
thomas.goto(-10,15)
thomas.pendown()
thomas.fillcolor("white")
thomas.begin_fill()
for i in range (0,10):
	thomas.fd(15)
	thomas.lt(36)
thomas.end_fill()
thomas.penup()

# Right Sclera
thomas.setheading(0)
thomas.goto(10,15)
thomas.pendown()
thomas.fillcolor("white")
thomas.begin_fill()
for i in range (0,10):
	thomas.fd(15)
	thomas.lt(36)
thomas.end_fill()
thomas.penup()

# Left Pupil
thomas.setheading(0)
thomas.goto(-10,17)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
thomas.circle(2)
thomas.end_fill()
thomas.penup()

# Right Pupil
thomas.setheading(0)
thomas.goto(-10,17)
thomas.pendown()
thomas.fillcolor("black")
thomas.begin_fill()
thomas.circle(2)
thomas.end_fill()
thomas.penup()

# Nose
thomas.setheading(0)
thomas.goto(-2,25)
thomas.pendown()
for i in range(0,9):
	thomas.lt(36)
	thomas.fd(3)
thomas.penup()

# Smile
thomas.goto(0,5)
thomas.pendown()
thomas.circle(5,180)

# Finishes
thomas.ht()
thomas.exitonclick()
