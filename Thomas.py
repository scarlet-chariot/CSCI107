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
wn = thomas.Screen() 	#creates new window entitled thomas
setup(width = 200, height = 200, startx = None, starty = None)	  #adjusts window size

# Background of thomas
thomas.penup()
thomas.goto(-40,-40)
thomas.pendown()
for i in range(0,4):
	thomas.forward(80)
	thomas.right(90)
	thomas.fillcolor(

