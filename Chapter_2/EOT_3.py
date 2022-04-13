from turtle import *

triangle_side_length = int(input("Enter the length of a side of the triangle: "))
triangle_base_angle = int(input("Enter the base angle of the triangle: "))

turtle = Turtle()

turtle.left(triangle_base_angle)
turtle.forward(triangle_side_length)
turtle.right(180-triangle_base_angle*2)
turtle.forward(triangle_side_length)
turtle.right(180-triangle_base_angle)
turtle.goto(0,0)

mainloop()
