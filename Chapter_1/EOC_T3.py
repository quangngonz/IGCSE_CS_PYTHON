from turtle import *

turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")

# draw pentagon with sides length of 100
for i in range(5):
    turtle.forward(100)
    turtle.left(72)

mainloop()