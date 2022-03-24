# Use turtle to draw a house
from turtle import *

turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")

# Draw a house
turtle.left(90)
turtle.forward(100)
turtle.right(45)
turtle.forward(156)
turtle.right(90)
turtle.forward(156)
turtle.right(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(220)

mainloop()
