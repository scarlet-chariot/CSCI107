#------------------------------------------------
# Alex Tseng
# March 23, 2018
# CSCI107
# Rance Harmon
#------------------------------------------------
# This program will generate a random number of
# randomly colored dots and prompt the user to 
# guess how many there are.
#------------------------------------------------

# setup
import turtle
import random

t= turtle.Turtle()
screen= turtle.Screen()
screen.setworldcoordinates(0,0,400,400)
t.speed(0)

# fucntions
def draw_dot(x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.dot(10,color)

#------------------------------------------------
n= random.randint(50,201)

#print(n) # for debugging purposes
c= 1
while c != n:
	x= random.randint(5,396)
	y= random.randint(5,396)
	color= random.choice(["red","blue","yellow","orange","green","purple"])
	draw_dot(x,y,color)
	c= c + 1

#print(c) # for debugging purposes

a= int(input("How many dots are on the screen: "))
b= 1
while a != n:
	if a > n and a <= 200:
		print("Your guess is too high. Try again.")
		a= int(input("How many dots are on the screen: "))
		b= b + 1
	elif a < n and a >= 50:
		print("Your guess is too low. Try again.")
		a= int(input("How many dots are on the screen: "))
		b= b + 1
	else:
		print("Your guess is out of the range, 50 and 200. Try again.")
		a= int(input("How many dots are on the screen: "))
print("The number of guesses you took was", str(b))
