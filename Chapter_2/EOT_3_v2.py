from turtle import *

triangle_side_length = int(input("Enter the length of a side of the triangle: "))

turtle = Turtle()

for i in range(3):
    turtle.forward(triangle_side_length)
    turtle.left(120)

mainloop()
