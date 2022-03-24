from turtle import * 

turtle = Turtle()
turtle.shape("turtle")
turtle.color("green")

#Draw a pentagon 
for i in range(5):
    turtle.forward(100)
    turtle.right(72)

mainloop()