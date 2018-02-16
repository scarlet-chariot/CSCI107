# -----------------------------------------+
# Shengnan Zhou, Alex Tseng                |
# CSCI 107, Assignment 4                   |
# Last Updated: February 16, 2018          |
# -----------------------------------------|
# Use loops to minimize repeated words and |
# phrases to these lyrics of "The Fox".    |
# -----------------------------------------+





print("Dog goes woof, cat goes meow.")
print("Bird goes tweet, and mouse goes squeak.")
print("Cow goes moo. Frog goes croak, and the elephant goes toot.")


a= "Ducks say quack and fish go blub, and the seal goes" 
for i in range(1,4):
	b= " OW"*i
print(a+b+".")

print("But there's one sound that no one knows...")
print("WHAT DOES THE FOX SAY?")



print()

for i in range(2):
	for j in range(4):
		c= " ding"*j+" dingeringeding!"
	print("Ring"+c)

print("Gering"+c)

for i in range(3):
	for j in range(6):
		d= " pa"*j+" pow!"
	print("Wa"+d)
